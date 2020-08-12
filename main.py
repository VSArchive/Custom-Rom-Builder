import os

print("########################################")
print("############### Devices ################")
print("########################################")
print("")

print("1.Redmi 7/Y3 (Onclite)")
print("99.Other")
print("")

deviceTree = ""
deviceBranch = ""
KernelTree = ""
KernelBranch = ""
vendorTree = ""
vendorBranch = ""

noOfDevices = 1  # For Now need to add more
deviceOption = int(input("Enter Option for Device : "))

if deviceOption > 0 and deviceOption <= noOfDevices:
    print("1.Lineage Os")
    print("2.AospExtended")
    print("3.Pixel Experience")
    print("4.Havoc OS")
    print("5.EvolutionX")
    print("6.Bliss Rom")
    print("7.MSM Xtended")
    print("8.DerpFest")
    print("9.Paranoid Android")
    print("10.Bootleggers ROM")
    print("")

romOption = int(input("Enter Option for Rom : "))


def initLineage():
    if os.path.exists("LineageOS") == False:
        os.system("mkdir LineageOS")
    os.chdir("LineageOS")
    os.system("repo init -u https://github.com/LineageOS/android.git -b lineage-17.1")


def initAospExtended():
    if os.path.exists("AospExtended") == False:
        os.system("mkdir AospExtended")
    os.chdir("AospExtended")
    os.system("repo init -u git://github.com/AospExtended/manifest.git -b 10.x")


def initPixelExperience():
    if os.path.exists("PixelExperience") == False:
        os.system("mkdir PixelExperience")
    os.chdir("PixelExperience")
    os.system("repo init -u https://github.com/PixelExperience/manifest -b ten")


def initHavocOS():
    if os.path.exists("HavocOS") == False:
        os.system("mkdir HavocOS")
    os.chdir("HavocOS")
    os.system("repo init -u https://github.com/Havoc-OS/android_manifest.git -b ten")


def initEvolutionX():
    if os.path.exists("EvolutionX") == False:
        os.system("mkdir EvolutionX")
    os.chdir("EvolutionX")
    os.system("repo init -u https://github.com/Evolution-X/manifest -b ten")


def initBlissRom():
    if os.path.exists("BlissRom") == False:
        os.system("mkdir BlissRom")
    os.chdir("BlissRom")
    os.system("repo init -u https://github.com/BlissRoms/platform_manifest.git -b q")


def initXtended():
    if os.path.exists("Xtended") == False:
        os.system("mkdir Xtended")
    os.chdir("Xtended")
    os.system("repo init -u https://github.com/Project-Xtended/manifest.git -b xq")  
    
    
def initDerpFest():
    if os.path.exists("DerpFest") == False:
        os.system("mkdir DerpFest")
    os.chdir("DerpFest")
    os.system("repo init -u git://github.com/DerpLab/platform_manifest.git -b ten")


def initParanoid():
    if os.path.exists("Paranoid") == False:
        os.system("mkdir Paranoid")
    os.chdir("Paranoid")
    os.system("repo init -u https://github.com/AOSPA/manifest -b quartz")


def initBootleggers():
    if os.path.exists("Bootleggers") == False:
        os.system("mkdir Bootleggers")
    os.chdir("Bootleggers")
    os.system("repo init -u https://github.com/BootleggersROM/manifest.git -b queso")


def sync():
    os.system("repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags")


def envsetup():
    os.system("source build/envsetup.sh")
    exitOption = input("If you want to customise any thing press (Y) to exit else (N) to continue to build (Y/N) : ")
    if exitOption == 'Y' or exitOption == 'y':
        exit
    elif exitOption == 'N' or exitOption == 'n':
        print("")
        print("########################################")
        print("########### Starting Build.. ###########")
        print("########################################")
        print("")


if deviceOption == 1:
    if os.path.exists("onclite") == False:
        os.system("mkdir onclite")
    os.chdir("onclite")
    if romOption == 1:
        initLineage()
        sync()
        gitVendor = "git clone https://github.com/vineelsai26/android_vendor_xiaomi_onclite.git vendor/xiaomi/onclite"
        os.system(gitVendor)
        envsetup()
        lunch = "breakfast onclite"
        os.system(lunch)
        os.system("croot")
        os.system("brunch onclite")

    elif romOption == 2:
        initAospExtended()
        sync()
        gitDevice = "git clone https://github.com/AospExtended-Devices/device_xiaomi_onclite.git device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/Dhina17/android_kernel_xiaomi_onclite.git -b 10.x kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/vineelsai26/android_vendor_xiaomi_onclite.git vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch aosp_onclite-userdebug"
        os.system(lunch)
        os.system("mka aex -j$(nproc --all)")

    elif romOption == 3:
        initPixelExperience()
        sync()
        gitDevice = "git clone https://github.com/vineelsai26/android_device_xiaomi_onclite.git -b 10 device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/vineelsai26/android_kernel_xiaomi_onclite.git -b 10 kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/vineelsai26/android_vendor_xiaomi_onclite.git -b 10 vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch aosp_onclite-userdebug"
        os.system(lunch)
        os.system("mka bacon -j$(nproc --all)")

    elif romOption == 4:
        initHavocOS()
        sync()
        gitDevice = "git clone https://github.com/Havoc-Devices/android_device_xiaomi_onclite.git device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/vineelsai26/android_kernel_xiaomi_onclite.git kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/vineelsai26/android_vendor_xiaomi_onclite.git vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch havoc_onclite-userdebug"
        os.system(lunch)

    elif romOption == 5:
        initEvolutionX()
        gitDevice = "git clone https://github.com/vineelsai26/android_device_xiaomi_onclite.git -b 10 device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/vineelsai26/android_kernel_xiaomi_onclite.git -b 10 kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/vineelsai26/android_vendor_xiaomi_onclite.git -b 10 vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch aosp_onclite-userdebug"
        os.system(lunch)
        os.system("mka bacon -j$(nproc --all)")

    elif romOption == 6:
        initBlissRom()
        sync()
        gitDevice = "git clone https://github.com/vineelsai26/android_device_xiaomi_onclite.git -b Bliss-12 device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/vineelsai26/android_kernel_xiaomi_onclite.git -b 10 kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/vineelsai26/android_vendor_xiaomi_onclite.git -b 10 vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "blissify bliss_onclite-userdebug"
        os.system(lunch)

    elif romOption == 7:
        initXtended()
        sync()
        gitDevice = "git clone https://github.com/Xtended-Devices/android_device_xiaomi_onclite.git device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/Xtended-Devices/android_kernel_xiaomi_onclite.git kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/Xtended-Devices/android_vendor_xiaomi_onclite.git vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch xtended_onclite-userdebug"
        os.system(lunch)
        os.system("make xtended")

    elif romOption == 8:
        initDerpFest()
        gitDevice = "git clone https://github.com/DerpFest-Devices/device_xiaomi_onclite.git device/xiaomi/onclite"
        gitKernel = "git clone https://github.com/DerpFest-Devices/kernel_xiaomi_onclite.git kernel/xiaomi/onclite"
        gitVendor = "git clone https://github.com/DerpFest-Devices/vendor_xiaomi_onclite.git vendor/xiaomi/onclite"
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch derp_onclite-userdebug"
        os.system(lunch)
        os.system("mka kronic")

    elif romOption == 9:
        print("comming soon...")
        # initParanoid()
        # sync()
        # os.system(gitDevice)
        # os.system(gitKernel)
        # os.system(gitVendor)
        # envsetup()
        # os.system("./rom-build.sh " + codeName)

    elif romOption == 10:
        print("comming soon...")
        # initBootleggers()
        # sync()
        # os.system(gitDevice)
        # os.system(gitKernel)
        # os.system(gitVendor)
        # envsetup()
        # lunch = "lunch bootleg_" + codeName + "-userdebug"
        # os.system(lunch)
        # os.system("mka bacon  -j$(nproc --all)")


elif deviceOption == 99:
    deviceTree = str(input("Enter device tree repo : "))
    deviceBranch = str(input("Enter device tree branch : "))
    KernelTree = str(input("Enter kernel tree repo : "))
    KernelBranch = str(input("Enter kernel tree branch : "))
    vendorTree = str(input("Enter vendor tree repo : "))
    vendorBranch = str(input("Enter vendor tree branch : "))

    brand = str(input("Enter Device brand : "))
    codeName = str(input("Enter Device code name : "))

    gitDevice = "git clone " + deviceTree + " -b " + deviceBranch + " device/" + brand + "/" + codeName
    gitKernel = "git clone " + KernelTree + " -b " + KernelBranch + " kernel/" + brand + "/" + codeName
    gitVendor = "git clone " + vendorTree + " -b " + vendorBranch + " vendor/" + brand + "/" + codeName
 
    if os.path.exists("android") == False:
        os.system("mkdir android")
    os.chdir("android")
    
    if romOption == 1:
        initLineage()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "breakfast" + codeName
        os.system(lunch)
        os.system("croot")
        os.system("brunch" + codeName)

    elif romOption == 2:
        initAospExtended()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch aosp_" + codeName + "-userdebug"
        os.system(lunch)
        os.system("mka aex -j$(nproc --all)")

    elif romOption == 3:
        initPixelExperience()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch aosp_" + codeName + "-userdebug"
        os.system(lunch)
        os.system("mka bacon -j$(nproc --all)")

    elif romOption == 4:
        initHavocOS()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch havoc_" + codeName + "-userdebug"
        os.system(lunch)

    elif romOption == 5:
        initEvolutionX()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch aosp_" + codeName + "-userdebug"
        os.system(lunch)
        os.system("mka bacon -j$(nproc --all)")

    elif romOption == 6:
        initBlissRom()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "blissify bliss_" + codeName + "-userdebug"
        os.system(lunch)

    elif romOption == 7:
        initXtended()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch xtended_" + codeName + "-userdebug"
        os.system(lunch)
        os.system("make xtended")

    elif romOption == 8:
        initDerpFest()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch derp_" + codeName + "-userdebug"
        os.system(lunch)
        os.system("mka kronic")

    elif romOption == 9:
        initParanoid()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        os.system("./rom-build.sh " + codeName)

    elif romOption == 10:
        initBootleggers()
        sync()
        os.system(gitDevice)
        os.system(gitKernel)
        os.system(gitVendor)
        envsetup()
        lunch = "lunch bootleg_" + codeName + "-userdebug"
        os.system(lunch)
        os.system("mka bacon  -j$(nproc --all)")

