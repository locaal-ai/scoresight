Get-ChildItem -Path translations -Filter *.ts | ForEach-Object {
    $tsFile = $_.FullName
    $poFile = [System.IO.Path]::ChangeExtension($tsFile, ".po")
    ts2po $tsFile $poFile
}
