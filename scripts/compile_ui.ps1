Get-ChildItem -Filter *.ui | ForEach-Object {
    $uiFile = $_.FullName
    $pyFile = [System.IO.Path]::ChangeExtension($uiFile, ".py")
    # add "ui_" prefix to the file name
    $pyFile = [System.IO.Path]::Combine($([System.IO.Path]::GetDirectoryName($pyFile)), "ui_$([System.IO.Path]::GetFileName($pyFile))")
    pyside6-uic $uiFile -o $pyFile
}
