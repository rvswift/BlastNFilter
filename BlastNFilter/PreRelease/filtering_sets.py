__author__ = 'robswift'

metals = set([' CP', 'NFU', 'NFR', 'NFE', 'NFV', 'FSO', 'WCC', 'TCN', 'FS2', 'PDV', 'CPT', 'OEC', 'XCC', 'NFS', 'C7P',
          'TBR', 'NFC', 'CUB', 'VA3', 'FV1', 'IME', 'FC6', 'RU7', 'TBY', 'REI', 'REJ', 'CNB', 'MM1', 'MM2', 'MM6',
          'MM5', 'YBT', 'CN1', 'CLF', 'CLP', 'NC1', 'V4O', 'HC0', 'VO3', 'CFM', 'CZL', 'CON', 'TBR', 'ICS', 'HCN',
          'CFN', 'CFC', 'HF3', 'ZRC', 'F3S', 'SRM', 'HDD'])

stabilisers = set(['B3P', 'PGE', '6JZ', '15P', 'PE3', 'XPE', '7PE', 'M2M', '13P', '3PP', 'PX4', '3OL', 'OC9', 'AE3', '6JZ',
               'XPE', '211', 'ODI', 'DIA', 'PG5', 'CXE', 'ME2', 'P4G', 'TOE', 'PG5', 'PE8', 'ZPG', 'PE3', 'MXE'])

buffers = set(['MPO', 'NHE', 'CXS', 'T3A', '3CX', '3FX', 'PIN'])

cofactors = set(["ATP", "ADP", "AMP", "ANP", "GTP", "GDP", "GNP", "UMP", "TTP", "TMP", "MGD", "H2U", "ADN", "APC", "M2G",
             "OMG", "OMC", "UDP", "UMP", "5GP", "5MU", "5MC", "2MG", "1MA", "NAD", "NAP", "NDP", "FAD", "FMN", "BH4",
             "BPH", "BTN", "PST", "SAM", "SAH", "COA", "ACO", "U10", "HEM", "HEC", "HEA", "HAS", "DHE", "BCL", "CLA",
             "6HE", "7HE", "DCP", "23T", "H4B", "WCC", "CFN", "AMP", "BCL", "BCB", "CHL", "NAP", "CON", "FAD", "NAD",
             "SXN", "U", "G", "QUY", "UDG", "CBY", "ST9", "25A", " A", " C", "B12", "HAS", "BPH", "BPB", "IPE", 'PLP',
             'H4B', 'PMP', 'PLP', 'TPP', 'TDP'])

#excipients = set("SO4", "SUL", " CL", " BR", " CA", " MG", " NI", " MN", " CU", "PO4", " CD", "NH4", " CO", " NA", "  K",
#              " ZN", " FE", "AZI", "A", "Ad", "C", "Cd", "CD", "CD2", "G", "Gd", "T", "Td", "A", "Ar", "Cr", "G", "Gr",
#              "U", "Ur", "YG", "I", "Ir", "CR", "CR2", "CR3", "CAC", "CO2", "CO3", "CYN", "FS4", "MO6", "NCO", "NO3",
#              "SCN", "SF4", " SE", " PB", "AU", "AU1", "AU3", "BR", "BR1", "CA", "CA2", "CL", "CL1", "CMP", "CO", "CO3",
#              "CPR", "CS", "CS1", "CU", "CU1", "CU2", "AG", "AG1", "AL", "AL3", "F", "F1", "FE", "FE2", "FE3", "IR",
#              "IR3", "K", "K1", "KR", "FUC", "MAN", "GAL", "MAL", "NAG", "GOL", "MPD", "BGC", "PEG", "EDO", "GLC",
#              "PG4", "BOG", "HTO", "ACX", "BMA", "FUC-a-L", "GAL-b-D", "GLC-b-D", "GCU", "GCU-b-D", "CEG", "CEG-b-D",
#              "MAN-b-D", "NAG-b-D", "RIB", "FRC", "FRU", "XYS", "XLS", "C8E", "CE9", "CRY", "DOX", "EGL", "F6P", "NDG",
#              "NGA", "P6G", "SIA", "SUC", "XYS", "1PE", "OLC", "POP", "MES", "EPE", "PYR", "GLC", "CIT", "FLC", "TAR",
#              "HC4", "MYR", "HED", "DTT", "BME", "TRS", "MPD", "ABA", "ACE", "ACT", "CME", "CSD", "CSO", "DMS", "EOH",
#              "FMT", "GTT", "HED", "IMD", "IOH", "IPA", "LDA", "LLP", "MYR", "PEP", "PYR", "PXY", "OXE", "TMT", "TMZ",
#              "2CV", "PLQ", "TAM", "1PG", "12P", "XP4", "PL3", "PE4", "PEU", "MPG", "B8M", "BOM", "B7M", "2PE", "STE",
#              "DME", "PLM", "PG0", "PE5", "PG6", "P33", "HEZ", "F23", "DTV", "SDS", "DTU", "DTD", "MRD", "MRY", "P33",
#              "BU1", "LHG", "D10", "OCT", "LI1", "ETE", "TZZ", "DEP", "DKA", "OLA", "MRD", "ACD", "MLR", "POG", "BTB",
#              "PC1", "ACY", " DT", "3GD", "MAE", "CA3", "144", "CP", "0KA", "A71", "UVW", "BET", "PBU", "UAP", "SER",
#              "CDL", "CEY", "LMN", "J7Z", "DA", "SIN", "  I", "PLC", "BME-BME", "FNE", "FUM", "MAK", " CP", "PAE",
#              "DTL", "HLT", "ASC", "FPP", "FII", "D1D", "PCT", "TTN", "HDA", "EDO-EDO", "PGA", "XXD", "INS", "217",
#              "BHL", "16D", "HSE", "OPE", "HCS", "SOR", "SKM", "KIV", "FCN", "TRA", "TRC", "MTL", "MZP", "KDG", "DHK")

junk = set(['AS8', 'PS9', 'CYI', 'NOB', 'DPO', 'MDN', 'APC', 'ACP', 'LPT', 'PBL', 'LFA', 'PGW', 'DD9', 'PGV', 'UPL', 'PEF',
        'MC3', 'LAP', 'PEE', 'D12', 'CXE', 'T1A', 'TBA', 'NET', 'NEH', 'P2N', 'PON', 'PIS', 'PPV', 'DPO', 'PSL', 'TLA',
        'SRT', '104', 'PTW', 'ACN', 'CHH', 'CCD', 'DAO', 'SBY', 'MYS', 'XPT', 'NM2', 'REE', 'SO4-SO4', 'P4C', 'C10',
        'PAW', 'OCM', '9OD', 'Q9C', 'UMQ', 'STP', 'PPK', '3PO', 'BDD', '5HD', 'YES', 'DIO', 'U10', 'C14', 'BTM', 'P03',
        'M21', 'PGV', 'LNK', 'EGC', 'BU3', 'R16', '4E6', '1EY', '1EX', 'B9M', 'LPP', 'IHD', 'NKR', 'T8X', 'AE4', 'X13',
        '16Y', 'B3P', 'RB3', 'OHA', 'DGG', 'HXA', 'D9G', 'HTG', 'B7G', 'FK9', '16P', 'SPM', 'TLA', 'B3P', '15P', 'SPO',
        'BCR', 'BCN', 'EPH', 'SPD', 'SPN', 'SPH', 'S9L', 'PTY', 'PE8', 'D12', 'PEK'])

saccharide = set(['NAG', 'MAN', 'BMA', 'FUC', 'GAL', 'BGC', 'GLC', 'NDG', 'BOG', 'SUC', 'XYP', 'FUL', 'MAL', 'GLA', 'LMT',
              'A2G', 'NGA', 'XYS', 'F6P', 'MMA', 'LAT', 'RAM', 'KDO', 'CBI', 'BNG', 'DMU', 'FBP', 'SGN', 'TRE', 'FRU',
              'PRP', 'IDS', 'CAP', 'BDP', 'AHR', 'GCU', 'ACR', 'G6P', 'BCD', 'ADA', 'DGD', 'BHG', 'SGC', 'IPT', 'G2F',
              'CTT', 'CBS', 'LBT', 'LMU', 'KDA', 'G6D', 'AAB', '5RP', 'NBG', 'FCA', 'SCR', 'RIP', 'RIB', 'ORP', 'MTT',
              'ASG', '6PG', 'R5P', 'MAG', 'GMH', 'G1P', 'NAA', 'GLP', 'GLO', 'GCD', 'XLS', 'FDP', 'BEM', 'ACX', '16G',
              'MGL', 'LGU', 'CTR', 'BGL', 'AMU', '2FP', 'XMM', 'SGA', 'RER', 'MFU', 'GLD', 'GCV', 'GCS', 'G16', 'FU4',
              'AGL', 'XUL', 'RNS', 'PA5', 'MBG', 'GYP', 'GCO', 'ASO', 'ARA', '149', 'R1P', 'MAW', 'M6P', 'LGC', 'GP1',
              'GAD', 'DAF', 'AGH', 'ABE', 'RUB', 'MXY', 'MAV', 'M8C', 'GCN', 'E4P', 'DFX', 'DDA', 'CTO', 'ARB', 'AAL',
              'TDG', 'GUP', 'GLF', 'GL0', 'G4D', 'FSI', 'BDR', 'ARE', 'AIG', '2FG', '147', 'TCB', 'SSG', 'S6P', 'RAF',
              'QPS', 'PSJ', 'NTP', 'NG6', 'MA3', 'IDY', 'HSX', 'GTR', 'GP4', 'GN1', 'GC4', 'FUD', 'FCB', 'ERI', 'ERE',
              'DVC', 'DQR', 'DDL', 'DAG', 'CT3', 'CBK', 'BXY', 'B9D', 'AOS', '1GL', 'RG1', 'NHF', 'MN0', 'MDA', 'LOG',
              'LAK', 'KO2', 'IDU', 'IDR', 'IDG', 'HSQ', 'GCT', 'G4S', 'FXP', 'FCT', 'DR2', 'DNO', 'DLG', 'BXX', 'BDG',
              'B4G', 'B2G', 'AXR', 'ABL', '3CM', '2DG', '10M', 'X2F', 'UCD', 'TYV', 'TOC', 'TOA', 'TAG', 'SUS', 'SUP',
              'SIO', 'RF5', 'RAT', 'R2B', 'PNG', 'NTO', 'NGY', 'NGS', 'NGE', 'NGC', 'NG1', 'MRP', 'MFB', 'MDM', 'MAB',
              'LSM', 'LCN', 'LB2', 'L6S', 'KBG', 'HSY', 'GU9', 'GU8', 'GU6', 'GU5', 'GU4', 'GU3', 'GU2', 'GU1', 'GU0',
              'GLS', 'G6S', 'G3I', 'FUB', 'FFC', 'F1P', 'EPG', 'EBG', 'DT6', 'DSR', 'DR4', 'DR3', 'DOM', 'DGS', 'CRA',
              'CR6', 'CEG', 'CDR', 'BXP', 'B6D', 'B0D', 'AXP', 'ARI', 'AFP', 'ABF', '7JZ', '5SP', '5GF', '3SA', '2M4',
              '2GL', '2FL', 'ZDM', 'XLF', 'XDP', 'XBP', 'X5S', 'X4S', 'VG1', 'UDC', 'TMX', 'TMR', 'TM9', 'TM6', 'TM5',
              'T6P', 'SOL', 'SOE', 'SHB', 'SG7', 'SG6', 'SG5', 'SG4', 'SDD', 'SA0', 'RST', 'RPA', 'RNT', 'RGG', 'REL',
              'RB5', 'RAO', 'RAE', 'R1X', 'QV4', 'QDK', 'PTQ', 'PSV', 'PNW', 'PNA', 'P6P', 'P53', 'P3M', 'OX2', 'OPM',
              'NYT', 'NXD', 'NTF', 'N1L', 'MUG', 'MMN', 'MLB', 'MG5', 'MDP', 'MCU', 'MAT', 'MA2', 'MA1', 'M3M', 'LXZ',
              'LXB', 'LTM', 'LOX', 'LM2', 'LDY', 'LAI', 'LAG', 'KTU', 'KO1', 'KFN', 'KDM', 'IN1', 'IDX', 'IAB', 'HSH',
              'HSG', 'HS2', 'HMS', 'HDL', 'H2P', 'GYV', 'GUZ', 'GUF', 'GTK', 'GTH', 'GS1', 'GPM', 'GPH', 'GNX', 'GLT',
              'GLG', 'GL9', 'GL7', 'GL6', 'GL5', 'GL2', 'GIV', 'GFP', 'GFG', 'GE1', 'GCW', 'GC1', 'GAC', 'FIX', 'FDQ',
              'F1X', 'EJT', 'EBQ', 'EAG', 'E5G', 'DRI', 'DQQ', 'DP5', 'DLF', 'DIG', 'DFR', 'DEL', 'D6G', 'CR1', 'CGF',
              'C5X', 'C4X', 'C3X', 'BXF', 'BMX', 'BGS', 'BGP', 'B8D', 'B16', 'AOG', 'ALL', 'AFR', 'AFO', 'AFD', 'AF1',
              'ACG', 'ABD', 'ABC', 'AAO', 'A1Q', '6SA', '5MM', '5DI', '50A', '4NN', '48Z', '46Z', '46M', '46D', '3MG',
              '3MF', '3LR', '3FM', '2M5', '293', '291', '289', '27C', '1JB', '1GN', '1BW', '18T', '15L', '14T', '0YT',
              '0XY', '0V4', '0TS', '0NZ', '0MK', '0BD', '045', 'BCN'])

do_not_call = set(['CP','NFU','NFR','NFE','NFV','FSO','WCC','TCN','FS2','PDV','CPT','OEC','XCC','NFS','C7P', 'TBR','NFC',
               'CUB','VA3','FV1','IME','FC6','RU7','TBY','REI','REJ','CNB','MM1','MM2','MM6', 'MM5','YBT','CN1','CLF',
               'CLP','V4O','HC0','VO3','CFM','CZL','CON','ICS','HCN','CFN','CFC', 'HF3','ZRC','F3S','SRM','HDD','B3P',
               'PGE','6JZ','15P','PE3','XPE','7PE','M2M','13P','3PP', 'PX4','3OL','OC9','AE3','211','ODI','DIA','PG5',
               'CXE','ME2','P4G','TOE','PE8','ZPG','MXE', 'MPO','NHE','CXS','T3A','3CX','3FX','PIN','MGD','NAD','NAP',
               'NDP','FAD','FMN','BH4','BPH', 'BTN','COA','ACO','U10','HEM','HEC','HEA','HAS','DHE','BCL','CLA','6HE',
               '7HE','H4B','BCB', 'CHL','SXN','QUY','UDG','CBY','ST9','25A','B12','BPB','IPE','PLP','PMP','TPP','TDP',
               'SO4', 'SUL','CL','BR','CA','MG','NI','MN','CU','PO4','CD','NH4','CO','NA','K','ZN', 'FE','AZI','CD2',
               'YG','CR','CR2','CR3','CAC','CO2','CO3','CYN','FS4','MO6','NCO','NO3', 'SCN','SF4','SE','PB','AU','AU3',
               'BR1','CA2','CL1','CS','CS1','CU1','AG','AG1','AL','AL3','F','FE2','FE3','IR','IR3','KR','MAL','GOL',
               'MPD','PEG','EDO','PG4','BOG','HTO', 'ACX','CEG','XLS','C8E','CE9','CRY','DOX','EGL','P6G','SUC','1PE',
               'OLC','POP','MES','EPE', 'PYR','CIT','FLC','TAR','HC4','MYR','HED','DTT','BME','TRS','ABA','ACE','ACT',
               'CME','CSD', 'CSO','DMS','EOH','FMT','GTT','IMD','IOH','IPA','LDA','LLP','PEP','PXY','OXE','TMT','TMZ',
               '2CV','PLQ','TAM','1PG','12P','XP4','PL3','PE4','PEU','MPG','B8M','BOM','B7M','2PE','STE', 'DME','PLM',
               'PG0','PE5','PG6','P33','HEZ','F23','DTV','SDS','DTU','DTD','MRD','MRY','BU1', 'LHG','D10','OCT','LI1',
               'ETE','TZZ','DEP','DKA','OLA','ACD','MLR','POG','BTB','PC1','ACY', '3GD','MAE','CA3','144','0KA','A71',
               'UVW','BET','PBU','SER','CDL','CEY','LMN','J7Z','SIN', 'PLC','FNE','FUM','MAK','PAE','DTL','HLT','FPP',
               'FII','D1D','PCT','TTN','HDA','PGA','XXD', 'INS','217','BHL','16D','HSE','OPE','HCS','SOR','SKM','KIV',
               'FCN','TRA','TRC','MTL','KDG', 'DHK','Ar', 'IOD', '35N', 'HGB', '3UQ'])