# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomizer_window.ui',
# licensing of 'randomizer_window.ui' applies.
#
# Created: Wed Nov  6 19:14:16 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 829, 631))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.seed = QtWidgets.QLineEdit(self.tab)
        self.seed.setObjectName("seed")
        self.gridLayout.addWidget(self.seed, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.clean_iso_path = QtWidgets.QLineEdit(self.tab)
        self.clean_iso_path.setObjectName("clean_iso_path")
        self.gridLayout.addWidget(self.clean_iso_path, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.output_folder = QtWidgets.QLineEdit(self.tab)
        self.output_folder.setObjectName("output_folder")
        self.gridLayout.addWidget(self.output_folder, 1, 1, 1, 1)
        self.output_folder_browse_button = QtWidgets.QPushButton(self.tab)
        self.output_folder_browse_button.setObjectName("output_folder_browse_button")
        self.gridLayout.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.clean_iso_path_browse_button = QtWidgets.QPushButton(self.tab)
        self.clean_iso_path_browse_button.setObjectName("clean_iso_path_browse_button")
        self.gridLayout.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.swift_sail = QtWidgets.QCheckBox(self.tab)
        self.swift_sail.setChecked(True)
        self.swift_sail.setObjectName("swift_sail")
        self.gridLayout.addWidget(self.swift_sail, 5, 0, 1, 1)
        self.increase_player_movement_speeds = QtWidgets.QCheckBox(self.tab)
        self.increase_player_movement_speeds.setChecked(True)
        self.increase_player_movement_speeds.setObjectName("increase_player_movement_speeds")
        self.gridLayout.addWidget(self.increase_player_movement_speeds, 9, 0, 1, 1)
        self.increase_grapple_animation_speed = QtWidgets.QCheckBox(self.tab)
        self.increase_grapple_animation_speed.setChecked(True)
        self.increase_grapple_animation_speed.setObjectName("increase_grapple_animation_speed")
        self.gridLayout.addWidget(self.increase_grapple_animation_speed, 8, 0, 1, 1)
        self.increase_block_moving_animation = QtWidgets.QCheckBox(self.tab)
        self.increase_block_moving_animation.setChecked(True)
        self.increase_block_moving_animation.setObjectName("increase_block_moving_animation")
        self.gridLayout.addWidget(self.increase_block_moving_animation, 7, 0, 1, 1)
        self.increase_misc_animations = QtWidgets.QCheckBox(self.tab)
        self.increase_misc_animations.setChecked(True)
        self.increase_misc_animations.setObjectName("increase_misc_animations")
        self.gridLayout.addWidget(self.increase_misc_animations, 10, 0, 1, 1)
        self.tingle_chests_without_tuner = QtWidgets.QCheckBox(self.tab)
        self.tingle_chests_without_tuner.setChecked(True)
        self.tingle_chests_without_tuner.setObjectName("tingle_chests_without_tuner")
        self.gridLayout.addWidget(self.tingle_chests_without_tuner, 12, 0, 1, 1)
        self.invert_camera_x_axis = QtWidgets.QCheckBox(self.tab)
        self.invert_camera_x_axis.setChecked(True)
        self.invert_camera_x_axis.setObjectName("invert_camera_x_axis")
        self.gridLayout.addWidget(self.invert_camera_x_axis, 17, 0, 1, 1)
        self.reveal_full_sea_chart = QtWidgets.QCheckBox(self.tab)
        self.reveal_full_sea_chart.setChecked(True)
        self.reveal_full_sea_chart.setObjectName("reveal_full_sea_chart")
        self.gridLayout.addWidget(self.reveal_full_sea_chart, 19, 0, 1, 1)
        self.KORL_control = QtWidgets.QCheckBox(self.tab)
        self.KORL_control.setChecked(True)
        self.KORL_control.setObjectName("KORL_control")
        self.gridLayout.addWidget(self.KORL_control, 15, 0, 1, 1)
        self.song_no_replay = QtWidgets.QCheckBox(self.tab)
        self.song_no_replay.setChecked(True)
        self.song_no_replay.setObjectName("song_no_replay")
        self.gridLayout.addWidget(self.song_no_replay, 16, 0, 1, 1)
        self.swing_turn = QtWidgets.QCheckBox(self.tab)
        self.swing_turn.setChecked(True)
        self.swing_turn.setObjectName("swing_turn")
        self.gridLayout.addWidget(self.swing_turn, 13, 0, 1, 1)
        self.remove_title_and_ending_videos = QtWidgets.QCheckBox(self.tab)
        self.remove_title_and_ending_videos.setChecked(True)
        self.remove_title_and_ending_videos.setObjectName("remove_title_and_ending_videos")
        self.gridLayout.addWidget(self.remove_title_and_ending_videos, 18, 0, 1, 1)
        self.ballad = QtWidgets.QCheckBox(self.tab)
        self.ballad.setChecked(True)
        self.ballad.setObjectName("ballad")
        self.gridLayout.addWidget(self.ballad, 14, 0, 1, 1)
        self.instant_text_boxes = QtWidgets.QCheckBox(self.tab)
        self.instant_text_boxes.setChecked(True)
        self.instant_text_boxes.setObjectName("instant_text_boxes")
        self.gridLayout.addWidget(self.instant_text_boxes, 6, 0, 1, 1)
        self.memorylogo = QtWidgets.QCheckBox(self.tab)
        self.memorylogo.setChecked(True)
        self.memorylogo.setObjectName("memorylogo")
        self.gridLayout.addWidget(self.memorylogo, 20, 0, 1, 1)
        self.titlelogo = QtWidgets.QCheckBox(self.tab)
        self.titlelogo.setChecked(True)
        self.titlelogo.setObjectName("titlelogo")
        self.gridLayout.addWidget(self.titlelogo, 21, 0, 1, 1)
        self.brisk_sail = QtWidgets.QCheckBox(self.tab)
        self.brisk_sail.setChecked(True)
        self.brisk_sail.setObjectName("brisk_sail")
        self.gridLayout.addWidget(self.brisk_sail, 22, 0, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.tab)
        self.label_81.setText("")
        self.label_81.setObjectName("label_81")
        self.gridLayout.addWidget(self.label_81, 23, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_for_custom_player_model = QtWidgets.QLabel(self.tab_2)
        self.label_for_custom_player_model.setObjectName("label_for_custom_player_model")
        self.horizontalLayout_3.addWidget(self.label_for_custom_player_model)
        self.custom_player_model = QtWidgets.QComboBox(self.tab_2)
        self.custom_player_model.setObjectName("custom_player_model")
        self.horizontalLayout_3.addWidget(self.custom_player_model)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.player_in_casual_clothes = QtWidgets.QCheckBox(self.tab_2)
        self.player_in_casual_clothes.setObjectName("player_in_casual_clothes")
        self.horizontalLayout_7.addWidget(self.player_in_casual_clothes)
        self.disable_custom_player_voice = QtWidgets.QCheckBox(self.tab_2)
        self.disable_custom_player_voice.setObjectName("disable_custom_player_voice")
        self.horizontalLayout_7.addWidget(self.disable_custom_player_voice)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        self.custom_model_comment = QtWidgets.QLabel(self.tab_2)
        self.custom_model_comment.setMaximumSize(QtCore.QSize(810, 16777215))
        self.custom_model_comment.setText("")
        self.custom_model_comment.setWordWrap(True)
        self.custom_model_comment.setObjectName("custom_model_comment")
        self.verticalLayout_3.addWidget(self.custom_model_comment)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.custom_colors_layout = QtWidgets.QVBoxLayout()
        self.custom_colors_layout.setObjectName("custom_colors_layout")
        self.verticalLayout_5.addLayout(self.custom_colors_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.custom_model_preview_label = QtWidgets.QLabel(self.tab_2)
        self.custom_model_preview_label.setText("")
        self.custom_model_preview_label.setObjectName("custom_model_preview_label")
        self.verticalLayout_6.addWidget(self.custom_model_preview_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea)
        self.option_description = QtWidgets.QLabel(self.centralwidget)
        self.option_description.setMinimumSize(QtCore.QSize(0, 18))
        self.option_description.setText("")
        self.option_description.setWordWrap(True)
        self.option_description.setObjectName("option_description")
        self.verticalLayout.addWidget(self.option_description)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.permalink = QtWidgets.QLabel(self.centralwidget)
        self.permalink.setObjectName("permalink")
        self.horizontalLayout_4.addWidget(self.permalink)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.update_checker_label = QtWidgets.QLabel(self.centralwidget)
        self.update_checker_label.setOpenExternalLinks(True)
        self.update_checker_label.setObjectName("update_checker_label")
        self.verticalLayout.addWidget(self.update_checker_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.reset_settings_to_default = QtWidgets.QPushButton(self.centralwidget)
        self.reset_settings_to_default.setMinimumSize(QtCore.QSize(180, 0))
        self.reset_settings_to_default.setObjectName("reset_settings_to_default")
        self.horizontalLayout.addWidget(self.reset_settings_to_default)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.randomize_button = QtWidgets.QPushButton(self.centralwidget)
        self.randomize_button.setObjectName("randomize_button")
        self.horizontalLayout.addWidget(self.randomize_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Better Wind Waker", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Clean Wind Waker Image", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Output Folder", None, -1))
        self.output_folder_browse_button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Patched Image Name", None, -1))
        self.clean_iso_path_browse_button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.swift_sail.setText(QtWidgets.QApplication.translate("MainWindow", "Swift Sail", None, -1))
        self.increase_player_movement_speeds.setText(QtWidgets.QApplication.translate("MainWindow", "Faster Rolling Speed", None, -1))
        self.increase_grapple_animation_speed.setText(QtWidgets.QApplication.translate("MainWindow", "Faster Grapple Hook", None, -1))
        self.increase_block_moving_animation.setText(QtWidgets.QApplication.translate("MainWindow", "Faster Block Moving", None, -1))
        self.increase_misc_animations.setText(QtWidgets.QApplication.translate("MainWindow", "Faster Crawling, Climbing, NPC zoom", None, -1))
        self.tingle_chests_without_tuner.setText(QtWidgets.QApplication.translate("MainWindow", "Tingle Chests Without Tuner", None, -1))
        self.invert_camera_x_axis.setText(QtWidgets.QApplication.translate("MainWindow", "Invert Camera", None, -1))
        self.reveal_full_sea_chart.setText(QtWidgets.QApplication.translate("MainWindow", "Reveal Sea Chart", None, -1))
        self.KORL_control.setText(QtWidgets.QApplication.translate("MainWindow", "Free-Roam Boat", None, -1))
        self.song_no_replay.setText(QtWidgets.QApplication.translate("MainWindow", "No Song Replays", None, -1))
        self.swing_turn.setText(QtWidgets.QApplication.translate("MainWindow", "Turn While Swinging/Grappling", None, -1))
        self.remove_title_and_ending_videos.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Intro Video", None, -1))
        self.ballad.setText(QtWidgets.QApplication.translate("MainWindow", "Faster Ballad of Gales", None, -1))
        self.instant_text_boxes.setText(QtWidgets.QApplication.translate("MainWindow", "Instant Text Boxes", None, -1))
        self.memorylogo.setText(QtWidgets.QApplication.translate("MainWindow", "Change Memory Card/Dolphin Logo", None, -1))
        self.titlelogo.setText(QtWidgets.QApplication.translate("MainWindow", "Change Title Screen Logo", None, -1))
        self.brisk_sail.setText(QtWidgets.QApplication.translate("MainWindow", "Brisk Sail", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Game Settings", None, -1))
        self.label_for_custom_player_model.setText(QtWidgets.QApplication.translate("MainWindow", "Player Model", None, -1))
        self.player_in_casual_clothes.setText(QtWidgets.QApplication.translate("MainWindow", "Casual Clothes", None, -1))
        self.disable_custom_player_voice.setText(QtWidgets.QApplication.translate("MainWindow", "Disable Custom Voice", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Cosmetic", None, -1))
        self.update_checker_label.setText(QtWidgets.QApplication.translate("MainWindow", "Checking for updates to the randomizer...", None, -1))
        self.about_button.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.reset_settings_to_default.setText(QtWidgets.QApplication.translate("MainWindow", "Reset All Settings to Default", None, -1))
        self.randomize_button.setText(QtWidgets.QApplication.translate("MainWindow", "Apply Patch", None, -1))

