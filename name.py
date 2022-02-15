import requests
from bs4 import BeautifulSoup
import os
os.system('clear a')
print ("""
	AFG--> Afganistan
	ALB--> Albania
	ALG--> Algeria
	SAA--> American Samoa
	AND--> Andorra
	AGL--> Angola
	AGI--> Anguilla
	ATG--> Antigua & Barbuda
	UAE--> Arab Emirates (United)
	ARG--> Argentina
	ARM--> Armenia
	ARU--> Aruba
	AUS--> Australia
	CHR--> Australia  Christmas Island
	NFK--> Australia  Norfolk
	AUT--> Austria
	AZE--> Azerbaijan
	AZR--> Azores
	BAH--> Bahamas
	BHR--> Bahrain
	BNG--> Bangladesh
	BRB--> Barbados
	BLR--> Belarus
	BEL--> Belgium
	BLZ--> Belize
	BEN--> Benin
	BER--> Bermuda
	BHU--> Bhutan
	BOL--> Bolivia
	BOS--> Bosnia & Herzegovina
	BOT--> Botswana
	BRA--> Brazil
	BRU--> Brunei Darussalam
	BUL--> Bulgaria
	BFS--> Burkina Faso
	MMR--> Burma (Myanmar)
	BDI--> Burundi
	CBG--> Cambodia
	CAM--> Cameroon
	CAN--> Canada
	ICA--> Canary Islands
	CAV--> Cape Verde
	CYM--> Cayman Islands
	CAF--> Central African Rep.
	TCD--> Chad
	JER--> Channel Islands
	CHL--> Chile
	CHN--> China
	HKG--> China  Hong Kong
	MAC--> China  Macau
	TAI--> China  Taiwan
	CHR--> Christmas Island
	COL--> Colombia
	COM--> Comoros
	COG--> Congo
	ZAI--> Congo Dem. Rep.
	COK--> Cook Islands
	CRI--> Costa Rica
	CRO--> Croatia
	CUB--> Cuba
	CYP--> Cyprus
	TCH--> Czech Rep.
	DNK--> Denmark
	FRO--> Denmark  Faroe Islands
	DJI--> Djibouti
	DMA--> Dominica
	DOM--> Dominican Rep.
	TIM--> East Timor
	ECU--> Ecuador
	EGY--> Egypt
	GNE--> Equatorial Guinea
	ERI--> Eritrea
	EST--> Estonia
	ETH--> Ethiopia
	FLK--> Falkland Islands
	FRO--> Faroe Islands
	FIJ--> Fiji
	FIN--> Finland
	FRA--> France
	GDL--> France  Guadeloupe
	GIA--> France  French Guiana
	MTN--> France  Martinique
	MYT--> France  Mayotte
	NCL--> France  New Caledonia
	PFR--> France  French Polynesia
	REU--> France  Reunion
	SPM--> France  St-Pierre & Miquelon
	GAB--> Gabon
	GAM--> Gambia
	GEO--> Georgia
	GER--> Germany
	GHA--> Ghana
	GIB--> Gibraltar
	GBR--> Great Britain
	MAN--> Great Britain  Isle of Man
	JER--> Great Britain  Jersey & G.
	GRE--> Greece
	GRL--> Greenland
	GRD--> Grenada
	GDL--> Guadeloupe
	GUM--> Guam
	GTM--> Guatemala
	GIA--> Guiana (French)
	GUI--> Guinea
	GNB--> Guinea-Bissau
	GNE--> Guinea (Equat.)
	GUY--> Guyana
	HAI--> Haiti
	HAW--> Hawaii Islands
	HND--> Honduras
	HKG--> Hong Kong
	HUN--> Hungary
	ISL--> Iceland
	IND--> India
	IDN--> Indonesia
	IRQ--> Iraq
	IRN--> Iran
	IRL--> Ireland
	MAN--> Isle of Man
	ISR--> Israel
	ITA--> Italy
	CIV--> Ivory Coast
	JAM--> Jamaica
	JAP--> Japan
	JER--> Jersey & Guernsey
	JOR--> Jordan
	KAZ--> Kazakhstan
	KEN--> Kenya
	KIR--> Kiribati
	KOR--> Korea
	KUW--> Kuwait
	KGZ--> Kyrgyzstan
	LAO--> Laos
	LAT--> Latvia
	LIB--> Lebanon
	LSO--> Lesotho
	LBR--> Liberia
	LBY--> Libya
	LIE--> Liechtenstein
	LIT--> Lithuania
	LUX--> Luxembourg
	MAC--> Macau
	MKD--> Macedonia
	MAD--> Madagascar
	MDR--> Madeira
	MWI--> Malawi
	MLS--> Malaysia
	MLD--> Maldives
	MLI--> Mali
	MLT--> Malta
	MAN--> Man (Isle)
	MRN--> Mariana Islands
	MHL--> Marshall Islands
	MTN--> Martinique
	MRT--> Mauritania
	MRI--> Mauritius
	MYT--> Mayotte
	MEX--> Mexico
	MIC--> Micronesia
	MOL--> Moldova
	MCO--> Monaco
	MNG--> Mongolia
	MSR--> Montserrat
	MAR--> Morocco
	MOZ--> Mozambique
	MMR--> Myanmar
	NAM--> Namibia
	NRU--> Nauru
	NEP--> Nepal
	NED--> Netherlands
	ATN--> Netherlands Antilles
	NCL--> New Caledonia
	NZL--> New Zealand
	NIC--> Nicaragua
	NGR--> Niger
	NIU--> Niue
	NIG--> Nigeria
	NFK--> Norfolk
	MRN--> Northern Mariana Isl.
	NOR--> Norway
	OMA--> Oman
	PAK--> Pakistan
	PLW--> Palau
	PAL--> Palestine
	PAN--> Panama
	PNG--> Papua New Guinea
	PAR--> Paraguay
	PER--> Peru
	PHL--> Philippines
	PIT--> Pitcairn
	POL--> Poland
	PFR--> Polynesia (French)
	PRT--> Portugal
	AZR--> Portugal  Azores
	MDR--> Portugal  Madeira
	PRI--> Puerto Rico
	QAT--> Qatar
	REU--> Reunion
	ROM--> Romania
	RUS--> Russia
	RWA--> Rwanda
	SHE--> Saint Helena
	SKN--> Saint Kitts & Nevis
	SLU--> Saint Lucia
	SPM--> Saint Pierre & Miquelon
	VCT--> Saint Vincent & Grenadines
	SLV--> Salvador
	SAA--> Samoa (American)
	SAM--> Samoa (Western)
	SMR--> San Marino
	STP--> Sao Tome & Principe
	SAU--> Saudi Arabia
	SEN--> Senegal
	SEY--> Seychelles
	SLE--> Sierra Leone
	SGP--> Singapore
	SLO--> Slovakia
	SVN--> Slovenia
	SLM--> Solomon
	SOM--> Somalia
	SAF--> South Africa
	ESP--> Spain
	ICA--> Spain / Canary
	SRI--> Sri Lanka
	SDN--> Sudan
	SUR--> Suriname
	SWA--> Swaziland
	SWE--> Sweden
	SUI--> Switzerland
	SYR--> Syria
	TAI--> Taiwan
	TJK--> Tajikistan
	TZA--> Tanzania
	THA--> Thailand
	TOG--> Togo
	TOK--> Tokelau
	TON--> Tonga
	TRI--> Trinidad & Tobago
	TUN--> Tunisia
	TUR--> Turkey
	TKM--> Turkmenistan
	TCA--> Turks & Caicos Islands
	TUV--> Tuvalu
	UGA--> Uganda
	UKR--> Ukraine
	UAE--> United Arab Emirates
	GBR--> United Kingdom
	URU--> Uruguay
	USA--> USA
	ALA--> USA  Alaska
	HAW--> USA  Hawaii
	GUM--> USA  Guam
	SAA--> USA  American Samoa
	UZB--> Uzbekistan
	VAN--> Vanuatu
	VAT--> Vatican
	VEN--> Venezuela
	VTN--> Viet Nam
	VRG--> Virgin Island GB
	VIR--> Virgin Island US
	WAL--> Wallis & Futuna
	SAH--> Western Sahara
	SAM--> Western Samoa
	YEM--> Yemen
	YUG--> Yugoslavia
	ZAI--> Zaire (Congo Dem.Rep)
	ZAM--> Zambia
	ZIM--> Zimbabwe
""")
print("---------------------------------------------------------")
print("")
print("""Enter the country code
for example  IRN--> Iran
""")
print("")
print("coded by Amir Ali telegram me @Try_excep_t")
print("")
try:

    code = input("enter code-->")
    site = requests.get('https://top-names.info/names.php?S=M&P='+code)
    soup = BeautifulSoup(site.text, 'html.parser')
    for data in soup.find_all("font", {"class":"t12"}): 
        res = data.get_text()
        file_name2 = "test2.txt"
        file = open('name'+code+'.text', "a")
        file.write(res+'\n')
        file.close()
        print(res)
except:
    print("Turn on the filter breaker")
