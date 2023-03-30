# Set properties
$givenName = "Franz"
$lastName = "Ferdinand"
$displayName = "$givenName $lastName"
$userPrincipalName = "ferdi@GlobeXpower.com"
$samAccountName = "ferdinandf"
$office = "Springfield"
$department = "TPS Department"
$title = "TPS Reporting Lead"

# Password 
$password = ConvertTo-SecureString "Solarwinds123!" -AsPlainText -Force
$newUser.SetPassword($password)

# Create Object
$newUser = New-Object System.DirectoryServices.AccountManagement.UserPrincipal([System.DirectoryServices.AccountManagement.PrincipalContext]::Current)
$newUser.GivenName = $givenName
$newUser.Surname = $lastName
$newUser.DisplayName = $displayName
$newUser.UserPrincipalName = $userPrincipalName
$newUser.SamAccountName = $samAccountName
$newUser.EmailAddress = $userPrincipalName
$newUser.Office = $office
$newUser.Department = $department
$newUser.Title = $title
$newUser.Enabled = $true

# Finally Save
$newUser.Save()
