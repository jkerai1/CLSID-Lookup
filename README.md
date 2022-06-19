# CLSID-Lookup
Frustrated with not being able to find what applications use what corresponding CLSID , I made this as a nice lookup. Please feel free to fork and contribute missing CLSIDs

# Powershell Comamnd Used: 
Get-ItemProperty -Path "HKLM:\SOFTWARE\Classes\CLSID\*" `
    |select PSChildName,`(default`) |ft -auto * | clip
