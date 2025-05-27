Get-ItemProperty -Path "HKLM:\SOFTWARE\Classes\CLSID\*"|select PSChildName,`(default`) |ft -auto *| clip
# This could be turned into a cmdlet for repeated use
