cmake_minimum_required (VERSION 3.5)

find_package(Java REQUIRED)
include(UseJava)

enable_testing()

project (ShutterEncoder NONE)

set(CMAKE_JAVA_COMPILE_FLAGS "-source" "17" "-target" "17")

add_jar(ShutterEncoder 
    SOURCES
    src/application/Console.java
    src/application/Ftp.java
    src/application/Functions.java
    src/application/GOP.java
    src/application/GlobalKeyListener.java
    src/application/Informations.java
    src/application/RecordInputDevice.java
    src/application/ReducedWindow.java
    src/application/Renamer.java
    src/application/RenderQueue.java
    src/application/RoundedLineBorder.java
    src/application/SceneDetection.java
    src/application/Settings.java
    src/application/Shutter.java
    src/application/Splash.java
    src/application/SubtitlesEdit.java
    src/application/SubtitlesEmbed.java
    src/application/SubtitlesHelp.java
    src/application/SubtitlesTimeline.java
    src/application/Update.java
    src/application/Utils.java
    src/application/VideoPlayer.java
    src/application/VideoWeb.java
    src/functions/AudioEncoders.java
    src/functions/AudioNormalization.java
    src/functions/BlackDetection.java
    src/functions/Command.java
    src/functions/Conform.java
    src/functions/DVDRIP.java
    src/functions/Extract.java
    src/functions/LoudnessTruePeak.java
    src/functions/Merge.java
    src/functions/OfflineDetection.java
    src/functions/Picture.java
    src/functions/ReplaceAudio.java
    src/functions/Rewrap.java
    src/functions/VMAF.java
    src/functions/VideoEncoders.java
    src/functions/VideoInserts.java
    src/library/BMXTRANSWRAP.java
    src/library/DCRAW.java
    src/library/DVDAUTHOR.java
    src/library/EXIFTOOL.java
    src/library/FFMPEG.java
    src/library/FFPROBE.java
    src/library/MEDIAINFO.java
    src/library/NCNN.java
    src/library/PDF.java
    src/library/SEVENZIP.java
    src/library/TSMUXER.java
    src/library/YOUTUBEDL.java
    src/settings/AdvancedFeatures.java
    src/settings/AudioSettings.java
    src/settings/BitratesAdjustement.java
    src/settings/Colorimetry.java
    src/settings/Corrections.java
    src/settings/Filter.java
    src/settings/FunctionUtils.java
    src/settings/Image.java
    src/settings/ImageSequence.java
    src/settings/InputAndOutput.java
    src/settings/Overlay.java
    src/settings/Timecode.java
    src/settings/Transitions.java
    RESOURCES NAMESPACE "contents"
    src/contents/2013-2016.jpg
    src/contents/arrow.svg
    src/contents/avid.png
    src/contents/complete.wav
    src/contents/davinci.png
    src/contents/error.wav
    src/contents/help.svg
    src/contents/help_hover.svg
    src/contents/help_pressed.svg
    src/contents/icon.png
    src/contents/item.svg
    src/contents/list.svg
    src/contents/list_hover.svg
    src/contents/list_pressed.svg
    src/contents/lock.svg
    src/contents/mail.svg
    src/contents/max.svg
    src/contents/max_hover.svg
    src/contents/max_pressed.svg
    src/contents/new.svg
    src/contents/new_hover.svg
    src/contents/new_pressed.svg
    src/contents/premiere.png
    src/contents/presets.svg
    src/contents/presets_hover.svg
    src/contents/presets_pressed.svg
    src/contents/preview.svg
    src/contents/preview_hover.svg
    src/contents/quit.svg
    src/contents/quit_hover.svg
    src/contents/quit_pressed.svg
    src/contents/reduce.svg
    src/contents/reduce_hover.svg
    src/contents/reduce_pressed.svg
    src/contents/settings.svg
    src/contents/settings_hover.svg
    src/contents/settings_pressed.svg
    src/contents/stream.svg
    src/contents/unlock.svg
    INCLUDE_JARS
    lib/activation.jar
    lib/commons-io-2.5.jar
    lib/commons-net-3.5.jar
    lib/flatlaf-3.3.jar
    lib/flatlaf-extras-3.3.jar
    lib/javax.mail.jar
    lib/jgoodies-common-1.8.0.jar
    lib/jgoodies-forms-1.8.0.jar
    lib/jnativehook-2.2.1.jar
    lib/jsoup-1.9.1.jar
    lib/jsvg-1.0.0.jar
    lib/pdfbox-app-2.0.28.jar
    lib/slf4j-api-1.7.9.jar
    lib/slf4j-simple-1.7.9.jar
    lib/swt-x86.jar
    lib/swt.jar
    ENTRY_POINT
    application.Shutter)

install_jar(ShutterEncoder /app/bin)
#include(GNUInstallDirs)
install(FILES lib/activation.jar
              lib/commons-io-2.5.jar
              lib/commons-net-3.5.jar
              lib/flatlaf-3.3.jar
              lib/flatlaf-extras-3.3.jar
              lib/javax.mail.jar
              lib/jgoodies-common-1.8.0.jar
              lib/jgoodies-forms-1.8.0.jar
              lib/jnativehook-2.2.1.jar
              lib/jsoup-1.9.1.jar
              lib/jsvg-1.0.0.jar
              lib/pdfbox-app-2.0.28.jar
              lib/slf4j-api-1.7.9.jar
              lib/slf4j-simple-1.7.9.jar
              lib/swt-x86.jar
              lib/swt.jar
        DESTINATION ${CMAKE_INSTALL_LIBDIR})
install(FILES Languages/de.properties
              Languages/en.properties
              Languages/es.properties
              Languages/fr.properties
              Languages/it.properties
              Languages/ja.properties
              Languages/nl.properties
              Languages/pl.properties
              Languages/pt_BR.properties
              Languages/ru.properties
              Languages/sl.properties
              Languages/sv.properties
              Languages/tr.properties
              Languages/uk.properties
              Languages/vi.properties
              Languages/zh_CN.properties
              Languages/zh_TW.properties
        DESTINATION ${CMAKE_INSTALL_BINDIR}/Languages) 
install(PROGRAMS ShutterEncoder.sh
        DESTINATION ${CMAKE_INSTALL_BINDIR})
install(DIRECTORY DESTINATION ${CMAKE_INSTALL_LIBDIR}/ffmpeg)

