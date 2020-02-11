#Imports
import sys, os, pygame, glob
from tinytag import TinyTag

#PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

#MyModules
from beta_2 import *

class ThreadClass(QThread):
    next_music = pyqtSignal(float)

    def __init__(self, parent=None):
        super(ThreadClass,self).__init__(parent)

    def run(self):
        while True:
            val = 1
            QThread.msleep(100)
            self.next_music.emit(val)

class MyWin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sm = 0
        self.s1 = 0
        self.s2 = 0

        # Pygame
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.set_endevent(2)

        # SliderInitValue
        self.ui.horizontalSlider.setValue(30)
        self.ui.horizontalSlider.setTickPosition(1)
        self.ui.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        cmbBoxArgs = ["A to Z",'Z to A','Date added','Artist']
        self.ui.cmbSort.addItems(cmbBoxArgs)

        #ConnectEvent
        self.ui.btnPlay.clicked.connect(self.Play)
        self.ui.btnPlay.clicked.connect(self.next_music)
        self.ui.btnPrev.clicked.connect(self.Prev)
        self.ui.btnNext.clicked.connect(self.Next)
        self.ui.btnSound.clicked.connect(self.SoundOff)
        self.ui.btnImport.clicked.connect(self.file_dialog)

        self.ui.horizontalSlider.valueChanged.connect(self.SoundChange)
        self.ui.cmbSort.currentIndexChanged.connect(self.Sort)
        self.ui.timeOfMusic.sliderReleased.connect(self.musTimeChange)
        self.ui.playList.currentRowChanged.connect(self.RowChange)


        #PlaylistInit
        self.folders = [""]
        self.songlist = []
        self.fileSong = []

        #ThreadINit
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.threadclass.next_music.connect(self.next_music)

    def file_dialog(self):
        dialog_name = "Choose File"
        folder_init_name = r'C:\Users\User\Desktop\Music\Playlist'
        folderName = QFileDialog.getExistingDirectory(self, dialog_name, folder_init_name)
        if self.folders.count(folderName) == 0:
            self.folders.append(folderName)

            #Changes the current directory
            os.chdir(self.folders[len(self.folders) - 1 ])

            self.songlist += glob.glob('**.mp3')
            for song in self.songlist:
                if self.songlist.count(song) > 1:
                    self.songlist.remove(song)
            #Takes all mp3 items in the current directory
            self.ui.playList.clear()
            self.ui.playList.addItems(self.songlist)
        else:
            print("The folder is null or empty")

    def next_music(self, val):
        if pygame.mixer.music.get_endevent() == 0 or pygame.mixer.music.get_pos() != -1:

            #MuicSlider
            tag = TinyTag.get(self.songlist[self.ui.playList.currentRow()])
            songDuration = round(tag.duration * 1000)
            self.ui.timeOfMusic.setMaximum(songDuration)
            self.ui.timeOfMusic.setValue(self.ui.timeOfMusic.value() + 100)

            #MusicStartLabel
            muzTimeValue = self.ui.timeOfMusic.value() / 1000
            self.m = int(muzTimeValue / 60)
            km = muzTimeValue - self.m * 60
            self.s1 = int(km // 10)
            self.s2 = int(km % 10)
            self.ui.muzStart.setText(str(self.m) + ':' + str(self.s1) +  str(self.s2))

            #Next Song
            muzTime = pygame.mixer.music.get_pos()
            if muzTime == -1 :
                QThread.msleep(1000)
                self.ui.playList.setCurrentRow(self.ui.playList.currentRow() + 1)
                pygame.mixer.music.load(self.songlist[self.ui.playList.currentRow()])
                pygame.mixer.music.play()
                pygame.mixer.music.set_endevent(0)
                self.ui.btnPlay.setChecked(True)
                self.ui.timeOfMusic.setValue(0)
                self.song_end_label()
        elif pygame.mixer.music.get_endevent() == 1 or pygame.mixer.music.get_endevent() == 2:
            pass

    #FIXME!!!
    def musTimeChange(self):
        pygame.mixer.music.set_pos(round(self.ui.timeOfMusic.value() / 1000))
        QThread.msleep(1000)

    def RowChange(self):
        pygame.mixer.music.set_endevent(2)
        self.ui.btnPlay.setChecked(False)

    def Play(self):
        song = self.songlist[self.ui.playList.currentRow()]
        Busy = pygame.mixer.music.get_busy()
        if Busy == 0 or pygame.mixer.music.get_endevent() == 2:
            #Play
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(0)
            self.ui.timeOfMusic.setValue(0)

            #MusicEndLabel
            self.song_end_label()

        elif Busy == 1 and pygame.mixer.music.get_endevent() == 0:
            #Pause
            pygame.mixer.music.pause()
            pygame.mixer.music.set_endevent(1)

        elif Busy == 1 and pygame.mixer.music.get_endevent() == 1:
            #UnPause
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_endevent(0)

    def Prev(self):
        self.a = self.ui.playList.currentRow()
        if self.ui.playList.currentRow() <= -1:
            self.ui.playList.setCurrentRow(self.ui.playList.count() - 2)
        elif self.ui.playList.currentRow() > -1:
            self.ui.playList.setCurrentRow(self.ui.playList.currentRow() - 1)
        pygame.mixer.music.load(self.songlist[self.ui.playList.currentRow()])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(0)
        self.ui.timeOfMusic.setValue(0)
        self.ui.btnPlay.setChecked(True)

        # MusicEndLabel
        self.song_end_label()
    def Next(self):
        self.a = self.ui.playList.currentRow()
        if self.ui.playList.currentRow() <= -1:
            self.ui.playList.setCurrentRow(0)
        elif self.ui.playList.currentRow() > -1:
            self.ui.playList.setCurrentRow(self.ui.playList.currentRow() + 1)
        pygame.mixer.music.load(self.songlist[self.ui.playList.currentRow()])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(0)
        self.ui.timeOfMusic.setValue(0)
        self.ui.btnPlay.setChecked(True)

        # MusicEndLabel
        self.song_end_label()

    def SoundOff(self):
        soundVolume = pygame.mixer.music.get_volume()
        if(soundVolume != 0):
            pygame.mixer.music.set_volume(0)
            self.ui.horizontalSlider.setValue(0)
        elif(soundVolume == 0):
            pygame.mixer.music.set_volume(0.5)
            self.ui.horizontalSlider.setValue(50)

    def SoundChange(self):
        sound = self.ui.horizontalSlider.value() / 100
        pygame.mixer.music.set_volume(sound)
        if(sound > 0 and self.ui.btnSound.isChecked() == True):
            self.ui.btnSound.setChecked(False)
        elif(sound == 0 and self.ui.btnSound.isChecked() == False):
            self.ui.btnSound.setChecked(True)

    #FIXME!!
    def Sort(self):
        song = self.songlist[self.ui.playList.currentRow()]
        if self.ui.cmbSort.currentIndex() == 0:
            self.ui.playList.sortItems(0)
        elif self.ui.cmbSort.currentIndex() == 1:
            self.ui.playList.sortItems(1)
        elif self.ui.cmbSort.currentIndex() == 2:
            pass
        elif self.ui.cmbSort.currentIndex() == 3:
            pass

    def song_end_label(self):
        song = self.songlist[self.ui.playList.currentRow()]
        tag = TinyTag.get(song)
        eDur = tag.duration
        em = int(eDur / 60)
        km = eDur - em * 60
        es1 = int(km // 10)
        es2 = int(km % 10)
        self.ui.muzEnd.setText(str(em) + ':' + str(es1) + str(es2))

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information,title,body)
        dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

