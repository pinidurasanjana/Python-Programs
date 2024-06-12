sltouk = str("Srilanka->United-Kingdom")
sltojapan = str("Srilanka->Japan")
sltosingapore = str("Srilanka->Singapore")
sltoaus = str("Srilanka->Australia")
uktousa = str("United-Kingdom->USA")
japantousa = str("Japan->USA")
singaporetojapan = str("Singapore->Japan")
japantoaus = str("Japan->Australia")
singaporetoaus = str("Singapore->Australia")

sltouk_time = float(11.45)
uktousa4 = float(8)
sltojapan5= float(8)

staringcountry = input(str("Enter the Starting country: "))
destinationcountry = input(str("Enter the Destination country: "))

if staringcountry=="SL":
    if destinationcountry=="UK":
        print(sltouk+" "+str(sltouk_time))
    elif destinationcountry == "USA":
        print(sltouk+"->"+uktousa)
