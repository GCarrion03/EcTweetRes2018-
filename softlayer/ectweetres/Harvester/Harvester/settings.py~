# -*- coding: utf-8 -*-
#########################################################################################################
#
# Author: Gustavo Carrion
# Date: Aug-2015
# Name: settings.py
# Description: Configuration file that specifies generic harvest parameters like usernames / e-mails for automated responses
# Execution:   python harvester_classifier.py 1
#
#########################################################################################################



#Local CouchDB 
server = 'http://localhost:5984/'
vm_ip = 'node1:localhost' #just a description to be included on emails
database = '' #create empty
location = '' #create empty
admin_user = 'user' #Futon admin username
admin_pass = 'user' #Futon admin pass

#create variables for each quadrant
consumer_key = '' #create empty
consumer_secret = '' #create empty
access_token = '' #create empty
access_secret = '' #create empty
region_quadrant = '' #create empty
#Bounding Box:
locations = [] #create empty
tracks = '' #create empty
follows = '' #create empty

#Email default configurations:
smtp_server = 'smtp.gmail.com'
from_address = 'gcmlth2015@gmail.com'
to_address = 'gcarrion03@gmail.com'
from_password = '2015GCMLTH'
def_subject = 'Harvesting process status update'
smtp_port = 587

#Define Quadrant initialization:
# Description: 	Method to be called by the main harvester file this configuration file especifies the cuadrant for melbourne
#
def defineQuadrant(quadrant):

	global consumer_key
	global consumer_secret
	global access_token
	global access_secret
	global locations
	global tracks
	global follows
	global location
	global database
	global region_quadrant

#harvester configuration
	if quadrant == '1': #single harvester setup
		database = 'echarvestmain' #name of the couchdb used to store tweets
		location = 'HarvestEC' #emailing services description
		region_quadrant = '1' #description to be included on emailing services, may be the same as the value of quadrant
		consumer_key = 'EF6WH9n1hv0T8rAW3FqFWeFG6' #Twitter API user info. (example)
		consumer_secret = 'RmIDDsWpvR3QES64Sx6haMnqOG5BpZqOm0HjsqAMkQrlciqrth' #Twitter API user info. (example)
		access_token = '496692665-fsM9vJRP2S2FFDeGFd4ie3QdSZDYEJv5PD1jBadF' #Twitter API user info. (example)
		access_secret = 'qDMBmfraxTcGhY2BavCqt0rg9UMjow7oY8xnffWzBCTTe' #Twitter API user info. (example)
		#geo cuadrant:
		locations = []
		tracks= ['BarcelonaSCweb','CSEmelec','FEFecuador','LDU_Oficial','DCuencaOficial','elnacionalec','Hincha_Azul','SDQUITO','ECUADORolimpico','vamosazules','body_and_health','Aucas45','Irvin_Veloz','LigaAgenda','JPlayRaces','gyetenisclub']
		follows=['248877722','96039232','167046714','361343242','330021348','132547612','14369839','454132312','169627734','296239551','246112803','368472038','236983585','358954167','315585961','2806505887','259780884','317783903','555264023','250729244','143860873','214977276','743593404','80688967','449818902','418782370','56716207','3196292541','2710521499','347956997','599525093','348725063','185305650','369198132','1328399822','492412104','267158028','962737249','284031928','234024077','232237571','1390512968','159175408','291773990','304526698','254114111','252884601','540956292','465890294','1887756121','3110534385','101788047','271524726','240754635','776910906','56455194','449138842','289606342','173976615','2161627459','175825033','301084643','1098279542','65205231','175419025','388313534','3063048622','562343909','882582638','170479559','3044914493','1965740845','169098508','413694085','322843984','807870157','94009674','81691066','339716107','1024365918','108764205','291998242','148794487','322847441','284148966','153447983','1117140031','18338160','227466451','1413770556','2285622972','435882815','67665104','406744818','801736166','144889418','1570723766','312148756','515869169','381766129','355620207','78465034','138099903','1358190091','2499422425','1551251448','381140429','164803945','1660195272','545469601','2254238180','52111884','1578082904','240008178','545497664','398151205','179377091','191090099','1209756726','2285375413','974878770','545507629','145475909','238375442','601086194','757623228','1949675732','115444056','393687098','768542695','249823507','1428804114','2906743588','128267192','1055793966','2790366846','3305082185','2541575882']
#		locations = [-78.833770752, -0.1160430115 , -78.2061767578, 0.2107996953] 
#		tracks= #'de,primera,obra,zona,la,mucho,incluso,sabe,que,mientras,través,calle,el,además,último,interior,en,quien,madre,tampoco,y,momento,mis,música,a,millones,modo,ningún,los,esto,problemas,vista,se,españa,cinco,campo,del,hombre,carlos,buen,las,están,hombres,hubiera,un,pues,información,saber,por,hoy,ojos,obras,con,lugar,muerte,razón,no,madrid,nombre,ex,una,nacional,algunas,niños,su,trabajo,público,presencia,para,otras,mujeres,tema,es,mejor,siglo,dinero,al,nuevo,todavía,comisión'
#		follows=''
	if quadrant == '2': # harvester 2 setup
		database = 'echarvestmain' #name of the couchdb used to store tweets
		location = 'HarvestEC' #emailing services description
		region_quadrant = '2' #description to be included on emailing services, may be the same as the value of quadrant
		consumer_key = 'XjfFq0Cd4SyaxNHF4N7hZsrXN' #Twitter API user info. (example)
		consumer_secret = 'hdkMyIuCnaCBHYtzrxqV1BUpxMla5y9mY2MUFW71buAQXju3cy' #Twitter API user info. (example)
		access_token = '755151922831691776-rTnvKDMbQEtmhP6pggUAwatmLB7Uxpn' #Twitter API user info. (example)
		access_secret = 'qMThXpaGzFZ1tkhMIijZJHHeUtPhZEvJNGi1U7EBbMj1D' #Twitter API user info. (example)
		#geo cuadrant:
		locations = []
		tracks= ['ClaroEcua','MovistarEC','SweetandCoffee','BancoPacificoEC','CNT_EC','BancoPichincha','BancoGuayaquil','CocaColaEC','marathonsports_','DIRECTVEcuador','BiessEcuador','empresar','ClubPremiumEc','pilsener_light','PacifiCard','Payless_EC','BancoCentral_Ec','Sprite_Ec','SamsungEC','CFN_ECUADOR','Colineal_ec','NetlifeEcuador','McDonalds_Ecu','ChevroletEc','PetroamazonasEP','produbancoec','De_Prati','TuentiEC','LATAM_ECU','PilsenerEcuador','BaninterEc','BrahmaEc','BB_Soluciones','Juanmarcetec','DinersClubEC','Artefacta_ec','dm3deportes','Qbit_Ecuador','IIASACAT','ElBosqueEC','CNEL_EP','DiscoverECU','comandato','TrenEcuador','Budweiser_EC','ZhumirEcuador','BcoBolivariano','Innovering','FioravantiEc','LaLlave_Ec','HuaweiMobileEc','fybeca','DonCamaronEc','DasaniEcuador','PoweradeEcuador','PepsiEcuador','kiamotorsec','AlmacenesBoyaca','TempoDesign','Nestle_Ecuador','nissanecuador','hunterEcuador','PronacaOficial','guiaecuador','metrovisiongye','Indurama','KitKatEcuador','FUZETeaEC','Correos_Ecuador','Avianca_ec','FantaEc','SupermaxiEcu','TEAMProdECU','fulgoreEC','MetrodeQuito','BurgerKingEC','pharmacys','Cocolon1','marcimex_','BDEcuadorBP','ComputronNEWS','TropicalEC','SumbawaEcuador','BuenisimoKFC','LoteriaNacJBG','EPPETROECUADOR','ZILLAZec','todocomex','TridentEcuador','GuitigEC','AllYouNeedisEC','EcuadorTravel','MALLDELSOL_EC','EcuaPoll','FotoEcuador','VisitaQuito','parischiquitoo','ViajaPrimeroEC','AeropuertoUIO','CityMall_Gye','Sanmarinogye','malldelsur','VILLAGE_PLAZA','amalavidaEC','MunicipioCuenca','PHGEcuador','PlazaLagos','QuicentroShoppi','BuenVivir_EC','QuicentroSur','Mall_El_Fortin','prefecturaLoja','RiocentroShopEC','ConvencionesGye','SanLuis_UIO','ambientequito','condadoshopping','MiTierra_rest','GYE_AAG','EPMQuitoTurismo','MalteriaPlaza','granados_plaza','ElRecreoQuito','MALLDELRIO','locos_parrilla','MrDicto','MuseoCarmenAlto','OMNIHospital','RestauranteSur','PolicentroGye','museoalabado','H_UTPL','HospiKennedy','CCI_ECUADOR','Bless_Ecuador','interlab_ec','quitoairportc','medsteticaEc']
		follows=['112757144','15447575','2409683900','174825461','223707073','135955550','475329140','164872539','260852470','18481795','47498127','492680819','226365618','834173358','1708942279','2227625119']

 #Define a geo area to extract tweets from
	if quadrant == '3': #harvester 3 setup
		database = 'echarvestmain' #name of the couchdb used to store tweets
		location = 'HarvestEC' #emailing services description
		region_quadrant = '3' #description to be included on emailing services, may be the same as the value of quadrant
		consumer_key = 'v6vHSrnFnJsJetfrsKtYkdto7' #Twitter API user info. (example)
		consumer_secret = 'xiOFOHTc2psM5nXG3YfNpRDV3HQbpJy4aor05568ypQWYDzPCN' #Twitter API user info. (example)
		access_token = '755153671239921664-zqyL7SnGTA4usmndk3ECVoPReBg8xO1' #Twitter API user info. (example)
		access_secret = '8Ks87P3dZatELtarLtwTAZEBYdcNu2MrIOYdBEzlggMSg' #Twitter API user info. (example)
		#geo cuadrant:
		locations = [] 
		tracks=['MashiRafael','Presidencia_Ec','ppsesa','PoliciaEcuador','jaimenebotsaadi','IGecuador','MinInteriorEc','MauricioRodasEC','alcaldiagye','CTEcuador','CarlosVerareal','daloes10','Riesgos_Ec','ECU911_','JorgeGlas','LassoGuillermo','AsambleaEcuador','Seguridad_Ec','ComunicacionEc','TurismoEc','Salud_Ec','abdalabucaram','RicardoPatinoEC','CancilleriaEc','Ambiente_Ec','vinizeta','cnegobec','SenpladesEc','DeporteEc','jimmyjairala','Vice_Ec','Justicia_Ec','FiscaliaEcuador','PaulCarrascoC','DefensaEc','Educacion_Ec','MunicipioQuito','CJudicaturaEc','InclusionEc','PoliticaEc','fcorderoc','Cultura_Ec','Telecom_Ec','DEFENSORIAEC','RegistroCivilec','EduSuperiorEc','AdmPublicaEc','Ecuadorencifras','SocialEc','cruzrojaecuador','Louisss_ale','6SusanaGonzalez','FinanzasEc','Pro_Ecuador','martharoldos','MinEnergia','IEPI_Ecuador','EnergiaEc','PartidoAvanza','RescateAnimalEC','UDLAQuito','Maria_DuarteP','EstrategicosEc','ConocimientoEc','dometabacchi','CiudadYachay','LucioGutierrez3','utpl','uees_ec','ucatolicagye','espol','ATMGuayaquil','ApoyaAlEcuador','ciespal','ObrasQuito','AmazoniaEc','INSPI_ECUADOR','lacamaragye','unicefecuador','EmAseoQuito','SETEDIS','CorteConstEcu','FPolyUgarte','FuerzaAereaEc','PolEconomicaEc','ProalimentosEC','SeguridadeQuito','jbgorg','roxanasilvach','LuisMongeE','Becas_SENESCYT','Yasuni_VIVE','TesEcuador','QuitoFluye','IEPS_Ec','AdventistasEC','UISEK','CocoYunez_6','UIDEGuayaquil','dgac_ecuador','ChechiAlvarado','CentEstEspSanto','ucasagrande','cruzrojaguayas','JCQuinonez','UIDE','goberzamora','PrimeroEcuador','GoberTungurahua','EspochRio','UnivEcotec','diegosalgadorib','IDEbschool','Todo_TurismoEc','GuidoAlexJalil','loxaesmas','COCOAUSFQ','UNEMI_ec','liderazgoecu','UnidadPopularUP','competenciascnc','rompecabezas24','luisvillacism','ICP_UEES','fundaciontef_ec','pacoasan','aldeasosecuador','USFQ_Alumni','lacapig','MoisesTacle','CanadaEcuador','worldvisionEC','fundapi','usfq_deportes','USFQ_GOBE','ignacioxavier','USFQ_Derecho','ProCambalache'] 
		follows=['2227625119']
	if quadrant == '4': #harvester 4 setup
		database = 'echarvestmain' #name of the couchdb used to store tweets
		location = 'HarvestEC' #emailing services description
		region_quadrant = '4' #description to be included on emailing services, may be the same as the value of quadrant
		consumer_key = 'ETj0EjyZ5MDz7gVkq1J21hlgz' #Twitter API user info. (example)
		consumer_secret = 'tqdHNhk4bKjRxGitCbLGHvWr3BZrlbSvZLTS47QvYC2zU1FFEk' #Twitter API user info. (example)
		access_token = '3163170402-B8Z9sJaKHhxxSrICk9uJwbBbYXlUoMJuBR7XTAU' #Twitter API user info. (example)
		access_secret = 'LnQmzv1js4uRQQVH7Jm6HFM1FRTcJpt434kcz7HO37MU2' #Twitter API user info. (example)
		#geo cuadrant:
		locations = [] 
		tracks= ['ecuavisa','teleamazonasec','eluniversocom','tctelevision','elcomerciocom','EcuavisaInforma','RTSEcuador','Gamatvec','Expresoec','EcuadorTV','el_telegrafo','noticiasecuador','lahoraecuador','ecuainm','revistavistazo','estadioec','100xCientoFTBL','marcadorec','UNQuito','comunidadgye','hoycomec','ElCiudadano_ec','StudioFutbol','elnoticierotc','ECUAGOL','Gamanoticiasec','CanalRTU','radiopublicaEC','EcuavisaShow','ecuadorenvivo','mercurioec','eltiempocuenca','tomebamba','JuicioCrudo','CanalUnoTv','teleramaec','sucomentario','andesecuador','eldiarioec','JUANPABLOSICCO','noticierouno','labrujaecuador','enlineaok','estadiomag','larepublica_ec','DiarioExtraEc','GrupoTVCableEC','Gamatvdeportes','emelexistaradio','ExaFmEcuador','comunidadquito','PROGRAMALATV','los40ecuador','revgeneracion21','LaSuprema961','redigitalec','julgamentobruto','WQRadio_EC','mastermusicmarc','radiorumbagye','cosasecuador','revistalaonda','ElMatinalGamaTv','DeporteTA','RevistaHogar','RevistaEkos','notiecuadoradio','ElproductorEC','RTS_LaNoticiaEC','eluniverso','VIDACTIVAec','ElMercioEC','entresalidas','clarosportsec','ecua_foto','MILAGROCITY','BGmagazineec','NuevoTiempo_Ec','ZonaSurEcuador','ElMilagrenoEC','lunesdeportivo','RevistaGuc','ThinkTankONG','vivefit_com','AycitoTumbaco','HUANCAVILCA830','BananaSapiens','cristomorphosis']
		follows=['2541575882']
#[144.3336,-38.5030,145.8784,-37.1751] melb
	if quadrant == '5': #harvester 5 setup by geolocation
		database = 'echarvestmain' #name of the couchdb used to store tweets
		location = 'HarvestEC' #emailing services description
		region_quadrant = '5' #description to be included on emailing services, may be the same as the value of quadrant
		consumer_key = 'LtnxKVrcGbQXmL4FJ0v7E4IWi' #Twitter API user info. (example)
		consumer_secret = 'bZECLPJ6HeTT8WBEefUvfsVCYchZXJgjnUJWq6oIvN8hD24Pwa' #Twitter API user info. (example)
		access_token = '755199932760526848-uA9MxkyxeelK3E6NpnhyhaJ0XPyETDs' #Twitter API user info. (example)
		access_secret = 'lYpcpwyufyy8ZSatao2zgDfl873uRmrxtATxPyejhItLQ' #Twitter API user info. (example)
		#geo cuadrant:
		locations = [-78.8234710693, -0.4542112459 , -78.2116699219, 0.0178527829] 
		tracks=[]
		follows=[]
#[144.3336,-38.5030,145.8784,-37.1751] melb
