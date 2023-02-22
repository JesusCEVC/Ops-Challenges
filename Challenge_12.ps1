  $filename = "network_report.txt"

  function Get-IPv4Addresses {
    param(
    [string]$C:\Users\admin\Desktop\network_report.txt
    )
    Get-Content $C:\Users\admin\Desktop\network_report.txt | Select-String '192.168.254.62' | ForEach-Object {
      $_ -replace '.*: '
    }
  }

  ipconfig /all > $network_report.txt

  $ipv4Addresses = Get-IPv4Addresses $network_report.txt

  Write-Host "IPv4 Addresses:`n$ipv4Addresses"

  Remove-Item $network_report.txt
