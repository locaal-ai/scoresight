$root = Split-Path -Parent -Path $MyInvocation.MyCommand.Path
$translationsDir = Join-Path -Path $root -ChildPath "..\translations"

# Get all .ts files in the translations directory
$tsFiles = Get-ChildItem -Path $translationsDir -Filter "*.ts" -File

# Loop through each .ts file and run pyside6-lrelease
foreach ($tsFile in $tsFiles) {
    pyside6-lupdate . -ts $tsFile
}
