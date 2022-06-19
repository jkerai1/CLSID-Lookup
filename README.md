# CLSID-Lookup
CLISID reference sheet. A CLSID is a globally unique identifier that identifies a COM class object.

Frustrated with not being able to find what applications use what corresponding CLSID , I made this as a nice lookup. Please feel free to fork and contribute missing CLSIDs

# Powershell Command Used: 
Get-ItemProperty -Path "HKLM:\SOFTWARE\Classes\CLSID\*" `
    |select PSChildName,`(default`) |ft -auto * | clip
