Get-ItemProperty -Path "HKLM:\SOFTWARE\Classes\CLSID*" |select PSChildName,(default`) |ft -auto * | clip
