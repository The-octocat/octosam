# VM-Ubuntu - Team Services Build Agent and Cross-Platform SDKs installation

![Azure Public Test Date](https://azurequickstartsservice.blob.core.windows.net/badges/vsts-fullbuild-ubuntu-vm/PublicLastTestDate.svg)
![Azure Public Test Result](https://azurequickstartsservice.blob.core.windows.net/badges/vsts-fullbuild-ubuntu-vm/PublicDeployment.svg)

![Azure US Gov Last Test Date](https://azurequickstartsservice.blob.core.windows.net/badges/vsts-fullbuild-ubuntu-vm/FairfaxLastTestDate.svg)
![Azure US Gov Last Test Result](https://azurequickstartsservice.blob.core.windows.net/badges/vsts-fullbuild-ubuntu-vm/FairfaxDeployment.svg)

![Best Practice Check](https://azurequickstartsservice.blob.core.windows.net/badges/vsts-fullbuild-ubuntu-vm/BestPracticeResult.svg)
![Cred Scan Check](https://azurequickstartsservice.blob.core.windows.net/badges/vsts-fullbuild-ubuntu-vm/CredScanResult.svg)

[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fvsts-fullbuild-ubuntu-vm%2Fazuredeploy.json)
[![Visualize](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/visualizebutton.svg?sanitize=true)](http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fvsts-fullbuild-ubuntu-vm%2Fazuredeploy.json)

This template allows you to create an Ubuntu VM with a full cross-platform development environment to support:
* OpenJDK 7 and 8; 
* Ant, Maven and Gradle;
* npm and nodeJS;
* groovy and gulp;
* Gnu C and C++ along with make;
* Perl, Python, Ruby and Ruby on Rails;
* latest .NET Core;
* go; 
* Docker Engine and Compose; and
* the VSTS CoreCLR Linux Build Agent. 
(Build Agent available here: https://github.com/Microsoft/vsts-agent).

Alternately, you can use Docker to deploy an equivalent capability by using the Dockerfile provided here:
https://github.com/Microsoft/vsts-dockerfiles/tree/master/ubuntu-xplat-build

To learn more about Visual Studio Team Services (VSTS) and Team Foundation Server (TFS) support for Java, check out:
http://java.visualstudio.com/

## Before you Deploy to Azure

To create the VM, you will need to:

1. Know the Team Services URL (e.g. https://myaccount.visualstudio.com)

2. Create or obtain a Personal Access Token (PAT) from Team Services which has *"Build (read and execute)"* and *"Agent Pools (read, manage)"* priviledges/capabilities
(see https://www.visualstudio.com/en-us/docs/setup-admin/team-services/use-personal-access-tokens-to-authenticate).

3. Create or obtain a build agent pool in Team Services
(see https://www.visualstudio.com/en-us/docs/release/getting-started/configure-agents)

4. Decide on a name for your build agent (i.e. the name for your agent within the above pool).

## Verifying the Agent
Once the VM is successfully provisioned, Team Services build agent installation and initialization can be verified by accessing the the *Agent pools* tab under the Control panel for the Team Services account
(e.g. https://myaccount.visualstudio.com/_admin/_AgentPool).  You should be able to click on the build agent pool (from #3 above)
and see your agent listed by the name (used in #4 above).  If all is well, the colored bar to the left of the pool name should be green.
If the colored bar is red, or if the agent name does not appear in the specified pool, see below for debugging hints.

## Debugging Agent Failures
If the Azure portal under *Virtual machines* shows that your VM is *Running* (in the Status column) but either the build agent name does not 
show up under the build Agent Pool in Team Services OR the agent name does show up but has a red colored bar to the left of the name,
then you can SSH into the VM and check the installation log.  To do this:
* SSH into the VM using the name (or IP number) of the VM, and account name and the password you specified when setting up the VM.
(You can SSH from the command line of another computer or use a free tool such as MobaXterm).
* Once logged onto the VM, in the top directory of the account should be a file called *"vsts.install.log.txt"*.  Use the 
*cat* command to display its contents (i.e. **cat vsts.install.log.txt**).  Look for any errors in this file to indicate what failed 
in starting up the VSTS build agent.  The most common mistake is not having the correct permissions for the PAT (see #2 above for more guidance).
* If the agent started sucessfully and is running but an expected tool or software is not working from a build task (e.g. a build task can't find
maven or java or ...), then you can check the file *"install.progress.txt"* in the top level directory to see if one of the packages
may have failed to install or had errors (**cat install.progress.txt**).
# package-website
{
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.

# User-specific files
*.suo
*.user
*.userosscache
*.sln.docstates

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
bld/
[Bb]in/
[Oo]bj/

# Visual Studio 2015 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUNIT
*.VisualState.xml
TestResult.xml

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# DNX
project.lock.json
artifacts/

*_i.c
*_p.c
*_i.h
*.ilk
*.meta
*.obj
*.pch
*.pdb
*.pgc
*.pgd
*.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
*.log
*.vspscc
*.vssscc
.builds
*.pidb
*.svclog
*.scc

# Chutzpah Test files
_Chutzpah*

# Visual C++ cache files
ipch/
*.aps
*.ncb
*.opendb
*.opensdf
*.sdf
*.cachefile

# Visual Studio profiler
*.psess
*.vsp
*.vspx
*.sap

# TFS 2012 Local Workspace
$tf/

# Guidance Automation Toolkit
*.gpState

# ReSharper is a .NET coding add-in
_ReSharper*/
*.[Rr]e[Ss]harper
*.DotSettings.user

# JustCode is a .NET coding add-in
.JustCode

# TeamCity is a build add-in
_TeamCity*

# DotCover is a Code Coverage Tool
*.dotCover

# NCrunch
_NCrunch_*
.*crunch*.local.xml
nCrunchTemp_*

# MightyMoose
*.mm.*
AutoTest.Net/

# Web workbench (sass)
.sass-cache/

# Installshield output folder
[Ee]xpress/

# DocProject is a documentation generator add-in
DocProject/buildhelp/
DocProject/Help/*.HxT
DocProject/Help/*.HxC
DocProject/Help/*.hhc
DocProject/Help/*.hhk
DocProject/Help/*.hhp
DocProject/Help/Html2
DocProject/Help/html

# Click-Once directory
publish/

# Publish Web Output
*.[Pp]ublish.xml
*.azurePubxml
# TODO: Comment the next line if you want to checkin your web deploy settings 
# but database connection strings (with potential passwords) will be unencrypted
*.pubxml
*.publishproj

# NuGet Packages
*.nupkg
# The packages folder can be ignored because of Package Restore
**/packages/*
# except build/, which is used as an MSBuild target.
!**/packages/build/
# Uncomment if necessary however generally it will be regenerated when needed
#!**/packages/repositories.config
# NuGet v3's project.json files produces more ignoreable files
*.nuget.props
*.nuget.targets

# Microsoft Azure Build Output
csx/
*.build.csdef

# Microsoft Azure Emulator
ecf/
rcf/

# Microsoft Azure ApplicationInsights config file
ApplicationInsights.config

# Windows Store app package directory
AppPackages/
BundleArtifacts/

# Visual Studio cache files
# files ending in .cache can be ignored
*.[Cc]ache
# but keep track of directories ending in .cache
!*.[Cc]ache/

# Others
ClientBin/
~$*
*~
*.dbmdl
*.dbproj.schemaview
*.pfx
*.publishsettings
node_modules/
orleans.codegen.cs

# RIA/Silverlight projects
Generated_Code/

# Backup & report files from converting an old project file
# to a newer Visual Studio version. Backup files are not needed,
# because we have git ;-)
_UpgradeReport_Files/
Backup*/
UpgradeLog*.XML
UpgradeLog*.htm

# SQL Server files
*.mdf
*.ldf

# Business Intelligence projects
*.rdl.data
*.bim.layout
*.bim_*.settings

# Microsoft Fakes
FakesAssemblies/

# GhostDoc plugin setting file
*.GhostDoc.xml

# Node.js Tools for Visual Studio
.ntvs_analysis.dat

# Visual Studio 6 build log
*.plg

# Visual Studio 6 workspace options file
*.opt

# Visual Studio LightSwitch build output
**/*.HTMLClient/GeneratedArtifacts
**/*.DesktopClient/GeneratedArtifacts
**/*.DesktopClient/ModelManifest.xml
**/*.Server/GeneratedArtifacts
**/*.Server/ModelManifest.xml
_Pvt_Extensions

# Paket dependency manager
.paket/paket.exe

# FAKE - F# Make
.fake/

}
}
