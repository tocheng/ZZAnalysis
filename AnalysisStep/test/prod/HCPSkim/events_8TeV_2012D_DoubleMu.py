LEPTON_SETUP = 2012

IsMC = False
PD = "DoubleMu"
MCFILTER = ""
ELECORRTYPE = "Moriond2013"
APPLYELEREGRESSION = True
APPLYELECALIB = True
APPLYMUCORR = True

import os
PyFilePath = os.environ['CMSSW_BASE'] + "/src/ZZAnalysis/AnalysisStep/test/"
execfile(PyFilePath + "analyzer.py")        
execfile(PyFilePath + "prod/json_2012.py")      



process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.source.fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2375.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2435.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2437.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2445.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2470.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2494.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_252.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2546.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_260.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1152.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2657.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_116.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2810.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2820.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2833.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2840.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2875.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2879.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2889.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2905.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_3076.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_3157.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_391.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_44.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_470.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_546.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_684.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1017.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_769.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_770.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_806.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_812.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_909.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_132.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1379.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1441.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1497.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1512.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1525.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1046.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1577.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1672.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1674.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1687.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1720.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1773.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1774.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_178.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1798.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1869.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1876.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1908.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1933.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1080.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1947.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2083.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_215.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2185.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_1115.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2234.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2241.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2307.root',
    'root://eoscms//eos/cms/store/cmst3/user/cmgtools/CMG/DoubleMu/Run2012D-PromptReco-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_2308.root',
    )


# This is the full list of 2012D events, not only those for this final state
process.source.eventsToProcess = cms.untracked.VEventRange( *(
    '203894:159:153492389',
    '203909:94:79591576',
    '203912:107:138158269',
    '203912:315:375170336',
    '203987:407:477862388',
    '203992:2:2226124',
    '203994:89:97681811',
    '204113:489:734372568',
    '204113:526:784493856',
    '204114:301:327118504',
    '204250:233:293533566',
    '204544:183:263194986',
    '204544:341:455057868',
    '204564:559:615093780',
    '204564:580:637834076',
    '204564:888:947831202',
    '204564:927:983341399',
    '204567:15:10694986',
    '204576:281:433041030',
    '204577:599:723221073',
    '204577:779:923559431',
    '204577:1012:1164017963',
    '204599:204:293531622',
    '204599:325:493182154',
    '204601:443:539665282',
    '204601:832:947734353',
    '204601:988:1089558842',
    '205111:189:233725391',
    '205158:211:286147237',
    '205217:184:190051995',
    '205238:311:335391276',
    '205238:521:544499395',
    '205310:189:245339434',
    '205310:370:513078030',
    '205339:134:151083216',
    '205344:1053:1097456291',
    '205344:1156:1182195352',
    '205519:7:9172701',
    '205519:58:76880301',
    '205519:457:520953305',
    '205617:307:333246186',
    '205620:161:123983433',
    '205666:711:1023081043',
    '205667:185:194675981',
    '205667:272:291820678',
    '205683:272:353162207',
    '205694:120:127212682',
    '205694:836:758109065',
    '205718:403:674409735',
    '205781:230:356725032',
    '205781:236:363949741',
    '205781:435:592726525',
    '205781:458:617795227',
    '205826:82:55134076',
    '205826:283:401042600',
    '205826:295:420041037',
    '205826:419:599229718',
    '205834:49:70540430',
    '205921:279:434325086',
    '206066:143:139537140',
    '206088:275:388474764',
    '206102:124:132410624',
    '206243:157:217502611',
    '206243:260:402678830',
    '206243:537:807811295',
    '206246:34:36559877',
    '206246:804:723782287',
    '206246:1024:880143354',
    '206258:106:94049945',
    '206304:32:32432249',
    '206304:41:41830321',
    '206331:119:117626330',
    '206389:321:448152127',
    '206401:119:132706940',
    '206446:368:536901756',
    '206446:943:1239554802',
    '206446:1062:1374805900',
    '206466:145:269895230',
    '206466:260:463399210',
    '206466:314:546604424',
    '206476:181:231762704',
    '206477:182:276785714',
    '206478:21:28851117',
    '206478:142:188791841',
    '206484:279:389977932',
    '206512:380:503782832',
    '206512:424:564077915',
    '206512:616:802036099',
    '206512:1131:1365305751',
    '206513:300:278141880',
    '206542:222:389766970',
    '206542:503:779897196',
    '206573:3:5379966',
    '206575:58:85848214',
    '206594:114:123988832',
    '206594:225:322510503',
    '206596:278:311554008',
    '206596:623:685265684',
    '206598:429:355198224',
    '206744:136:178829388',
    '206744:390:553270298',
    '206745:58:67917612',
    '206859:271:395759900',
    '206859:391:594138345',
    '206859:663:971857351',
    '206859:688:1003127634',
    '207099:715:990710339',
    '207214:150:225528979',
    '207220:127:138519342',
    '207231:821:1154853710',
    '207231:999:1344760175',
    '207269:140:150711847',
    '207269:270:359837986',
    '207269:501:673638714',
    '207273:423:472815275',
    '207273:596:658418063',
    '207279:107:117459264',
    '207279:980:1269360116',
    '207320:290:236655047',
    '207397:144:245323981',
    '207397:173:295324467',
    '207454:254:384016969',
    '207454:359:554587442',
    '207454:587:873201612',
    '207454:1213:1580150704',
    '207454:1516:1880956584',
    '207477:447:708577972',
    '207477:532:829999596',
    '207477:558:865695065',
    '207487:146:225565614',
    '207487:217:356427819',
    '207487:388:630809308',
    '207490:76:82625945',
    '207492:81:68053600',
    '207492:252:206127288',
    '207515:137:169100521',
    '207515:490:773053910',
    '207515:503:792210029',
    '207886:70:80529749',
    '207905:422:616574429',
    '207922:3:2780787',
    '207922:85:96488947',
    '208307:769:1022410825',
    '208339:204:266730222',
    '208357:170:178044443',
    '208391:199:294437023',
    '208391:212:312032921',
    '208391:462:626206528',
    '208391:531:703712657',
    '208427:54:52300502',
    '208427:585:865434697',
    '208429:164:185785545',
    '208487:123:217609091',
    '208540:50:88111521',
    '208551:570:883384151',
    '208686:425:656049185',
))