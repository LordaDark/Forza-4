; Installer Forza 4
!include "MUI2.nsh"
!include "FileFunc.nsh"

; Metadati dell'applicazione
Name "Forza 4"
OutFile "Forza4_Setup.exe"
InstallDir "$PROGRAMFILES\Forza4"

; Richiedi privilegi di amministratore
RequestExecutionLevel admin

; Interfaccia
!define MUI_ABORTWARNING
!define MUI_ICON "src\assets\icon.ico"
!define MUI_UNICON "src\assets\icon.ico"

; Pagine dell'installer
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Pagine del disinstallatore
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

; Lingue
!insertmacro MUI_LANGUAGE "Italian"

; Sezioni dell'installer
Section "Forza 4 (richiesto)" SecMain
  SectionIn RO
  SetOutPath "$INSTDIR"
  
  ; Copia i file del gioco
  File /r "dist\*.*"
  
  ; Crea la directory per i punteggi
  CreateDirectory "$DOCUMENTS\Forza4"
  
  ; Crea il disinstallatore
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  ; Crea il menu Start
  CreateDirectory "$SMPROGRAMS\Forza4"
  CreateShortcut "$SMPROGRAMS\Forza4\Forza 4.lnk" "$INSTDIR\Forza4.exe"
  CreateShortcut "$SMPROGRAMS\Forza4\Disinstalla.lnk" "$INSTDIR\uninstall.exe"
  
  ; Registra l'applicazione
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Forza4" \
                 "DisplayName" "Forza 4"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Forza4" \
                 "UninstallString" "$INSTDIR\uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Forza4" \
                 "DisplayIcon" "$INSTDIR\Forza4.exe"
SectionEnd

Section "Collegamento sul Desktop" SecDesktop
  CreateShortcut "$DESKTOP\Forza 4.lnk" "$INSTDIR\Forza4.exe"
SectionEnd

Section "Aggiungi alla barra delle applicazioni" SecTaskbar
  CreateShortcut "$QUICKLAUNCH\Forza 4.lnk" "$INSTDIR\Forza4.exe"
SectionEnd

; Descrizioni delle sezioni
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SecMain} "Installa il gioco Forza 4."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "Crea un collegamento sul desktop."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecTaskbar} "Aggiunge il gioco alla barra delle applicazioni."
!insertmacro MUI_FUNCTION_DESCRIPTION_END

; Disinstallatore
Section "Uninstall"
  ; Rimuovi i file
  RMDir /r "$INSTDIR"
  RMDir /r "$DOCUMENTS\Forza4"
  RMDir /r "$SMPROGRAMS\Forza4"
  Delete "$DESKTOP\Forza 4.lnk"
  Delete "$QUICKLAUNCH\Forza 4.lnk"
  
  ; Rimuovi la registrazione
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Forza4"
SectionEnd