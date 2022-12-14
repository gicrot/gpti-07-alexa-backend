from utils import normalize

original_region_por_comuna = {
    "Arica":"15",
    "Camarones":"15",
    "Putre":"15",
    "General Lagos":"15",
    "Iquique":"01",
    "Alto Hospicio":"01",
    "Pozo Almonte":"01",
    "Camiña":"01",
    "Colchane":"01",
    "Huara":"01",
    "Pica":"01",
    "Antofagasta":"02",
    "Mejillones":"02",
    "Sierra Gorda":"02",
    "Taltal":"02",
    "Calama":"02",
    "Ollagüe":"02",
    "San Pedro de Atacama":"02",
    "Tocopilla":"02",
    "María Elena":"02",
    "Copiapó":"03",
    "Caldera":"03",
    "Tierra Amarilla":"03",
    "Chañaral":"03",
    "Diego de Almagro":"03",
    "Vallenar":"03",
    "Alto del Carmen":"03",
    "Freirina":"03",
    "Huasco":"03",
    "La Serena":"04",
    "Coquimbo":"04",
    "Andacollo":"04",
    "La Higuera":"04",
    "Paiguano":"04",
    "Vicuña":"04",
    "Illapel":"04",
    "Canela":"04",
    "Los Vilos":"04",
    "Salamanca":"04",
    "Ovalle":"04",
    "Combarbalá":"04",
    "Monte Patria":"04",
    "Punitaqui":"04",
    "Río Hurtado":"04",
    "Valparaíso":"05",
    "Casablanca":"05",
    "Concón":"05",
    "Juan Fernández":"05",
    "Puchuncaví":"05",
    "Quintero":"05",
    "Viña del Mar":"05",
    "Isla de Pascua":"05",
    "Los Andes":"05",
    "Calle Larga":"05",
    "Rinconada":"05",
    "San Esteban":"05",
    "La Ligua":"05",
    "Cabildo":"05",
    "Papudo":"05",
    "Petorca":"05",
    "Zapallar":"05",
    "Quillota":"05",
    "Calera":"05",
    "Hijuelas":"05",
    "La Cruz":"05",
    "Nogales":"05",
    "San Antonio":"05",
    "Algarrobo":"05",
    "Cartagena":"05",
    "El Quisco":"05",
    "El Tabo":"05",
    "Santo Domingo":"05",
    "San Felipe":"05",
    "Catemu":"05",
    "Llaillay":"05",
    "Panquehue":"05",
    "Putaendo":"05",
    "Santa María":"05",
    "Quilpué":"05",
    "Limache":"05",
    "Olmué":"05",
    "Villa Alemana":"05",
    "Rancagua":"06",
    "Codegua":"06",
    "Coinco":"06",
    "Coltauco":"06",
    "Doñihue":"06",
    "Graneros":"06",
    "Las Cabras":"06",
    "Machalí":"06",
    "Malloa":"06",
    "Mostazal":"06",
    "Olivar":"06",
    "Peumo":"06",
    "Pichidegua":"06",
    "Quinta de Tilcoco":"06",
    "Rengo":"06",
    "Requínoa":"06",
    "San Vicente":"06",
    "Pichilemu":"06",
    "La Estrella":"06",
    "Litueche":"06",
    "Marchihue":"06",
    "Navidad":"06",
    "Paredones":"06",
    "San Fernando":"06",
    "Chépica":"06",
    "Chimbarongo":"06",
    "Lolol":"06",
    "Nancagua":"06",
    "Palmilla":"06",
    "Peralillo":"06",
    "Placilla":"06",
    "Pumanque":"06",
    "Santa Cruz":"06",
    "Talca":"07",
    "Constitución":"07",
    "Curepto":"07",
    "Empedrado":"07",
    "Maule":"07",
    "Pelarco":"07",
    "Pencahue":"07",
    "Río Claro":"07",
    "San Clemente":"07",
    "San Rafael":"07",
    "Cauquenes":"07",
    "Chanco":"07",
    "Pelluhue":"07",
    "Curicó":"07",
    "Hualañé":"07",
    "Licantén":"07",
    "Molina":"07",
    "Rauco":"07",
    "Romeral":"07",
    "Sagrada Familia":"07",
    "Teno":"07",
    "Vichuquén":"07",
    "Linares":"07",
    "Colbún":"07",
    "Longaví":"07",
    "Parral":"07",
    "Retiro":"07",
    "San Javier":"07",
    "Villa Alegre":"07",
    "Yerbas Buenas":"07",
    "Cobquecura":"16",
    "Coelemu":"16",
    "Ninhue":"16",
    "Portezuelo":"16",
    "Quirihue":"16",
    "Ránquil":"16",
    "Treguaco":"16",
    "Bulnes":"16",
    "Chillán Viejo":"16",
    "Chillán":"16",
    "El Carmen":"16",
    "Pemuco":"16",
    "Pinto":"16",
    "Quillón":"16",
    "San Ignacio":"16",
    "Yungay":"16",
    "Coihueco":"16",
    "Ñiquén":"16",
    "San Carlos":"16",
    "San Fabián":"16",
    "San Nicolás":"16",
    "Concepción":"08",
    "Coronel":"08",
    "Chiguayante":"08",
    "Florida":"08",
    "Hualqui":"08",
    "Lota":"08",
    "Penco":"08",
    "San Pedro de la Paz":"08",
    "Santa Juana":"08",
    "Talcahuano":"08",
    "Tomé":"08",
    "Hualpén":"08",
    "Lebu":"08",
    "Arauco":"08",
    "Cañete":"08",
    "Contulmo":"08",
    "Curanilahue":"08",
    "Los Álamos":"08",
    "Tirúa":"08",
    "Los Ángeles":"08",
    "Antuco":"08",
    "Cabrero":"08",
    "Laja":"08",
    "Mulchén":"08",
    "Nacimiento":"08",
    "Negrete":"08",
    "Quilaco":"08",
    "Quilleco":"08",
    "San Rosendo":"08",
    "Santa Bárbara":"08",
    "Tucapel":"08",
    "Yumbel":"08",
    "Alto Biobío":"08",
    "Temuco":"09",
    "Carahue":"09",
    "Cunco":"09",
    "Curarrehue":"09",
    "Freire":"09",
    "Galvarino":"09",
    "Gorbea":"09",
    "Lautaro":"09",
    "Loncoche":"09",
    "Melipeuco":"09",
    "Nueva Imperial":"09",
    "Padre las Casas":"09",
    "Perquenco":"09",
    "Pitrufquén":"09",
    "Pucón":"09",
    "Saavedra":"09",
    "Teodoro Schmidt":"09",
    "Toltén":"09",
    "Vilcún":"09",
    "Villarrica":"09",
    "Cholchol":"09",
    "Angol":"09",
    "Collipulli":"09",
    "Curacautín":"09",
    "Ercilla":"09",
    "Lonquimay":"09",
    "Los Sauces":"09",
    "Lumaco":"09",
    "Purén":"09",
    "Renaico":"09",
    "Traiguén":"09",
    "Victoria":"09",
    "Valdivia":"14",
    "Corral":"14",
    "Lanco":"14",
    "Los Lagos":"14",
    "Máfil":"14",
    "Mariquina":"14",
    "Paillaco":"14",
    "Panguipulli":"14",
    "La Unión":"14",
    "Futrono":"14",
    "Lago Ranco":"14",
    "Río Bueno":"14",
    "Puerto Montt":"10",
    "Calbuco":"10",
    "Cochamó":"10",
    "Fresia":"10",
    "Frutillar":"10",
    "Los Muermos":"10",
    "Llanquihue":"10",
    "Maullín":"10",
    "Puerto Varas":"10",
    "Castro":"10",
    "Ancud":"10",
    "Chonchi":"10",
    "Curaco de Vélez":"10",
    "Dalcahue":"10",
    "Puqueldón":"10",
    "Queilén":"10",
    "Quellón":"10",
    "Quemchi":"10",
    "Quinchao":"10",
    "Osorno":"10",
    "Puerto Octay":"10",
    "Purranque":"10",
    "Puyehue":"10",
    "Río Negro":"10",
    "San Juan de la Costa":"10",
    "San Pablo":"10",
    "Chaitén":"10",
    "Futaleufú":"10",
    "Hualaihué":"10",
    "Palena":"10",
    "Coihaique":"11",
    "Lago Verde":"11",
    "Aisén":"11",
    "Cisnes":"11",
    "Guaitecas":"11",
    "Cochrane":"11",
    "O’Higgins":"11",
    "Tortel":"11",
    "Chile Chico":"11",
    "Río Ibáñez":"11",
    "Punta Arenas":"12",
    "Laguna Blanca":"12",
    "Río Verde":"12",
    "San Gregorio":"12",
    "Cabo de Hornos (Ex Navarino)":"12",
    "Antártica":"12",
    "Porvenir":"12",
    "Primavera":"12",
    "Timaukel":"12",
    "Natales":"12",
    "Torres del Paine":"12",
    "Cerrillos":"13",
    "Cerro Navia":"13",
    "Conchalí":"13",
    "El Bosque":"13",
    "Estación Central":"13",
    "Huechuraba":"13",
    "Independencia":"13",
    "La Cisterna":"13",
    "La Florida":"13",
    "La Granja":"13",
    "La Pintana":"13",
    "La Reina":"13",
    "Las Condes":"13",
    "Lo Barnechea":"13",
    "Lo Espejo":"13",
    "Lo Prado":"13",
    "Macul":"13",
    "Maipú":"13",
    "Ñuñoa":"13",
    "Pedro Aguirre Cerda":"13",
    "Peñalolén":"13",
    "Providencia":"13",
    "Pudahuel":"13",
    "Quilicura":"13",
    "Quinta Normal":"13",
    "Recoleta":"13",
    "Renca":"13",
    "Santiago":"13",
    "San Joaquín":"13",
    "San Miguel":"13",
    "San Ramón":"13",
    "Vitacura":"13",
    "Puente Alto":"13",
    "Pirque":"13",
    "San José de Maipo":"13",
    "Colina":"13",
    "Lampa":"13",
    "Tiltil":"13",
    "San Bernardo":"13",
    "Buin":"13",
    "Calera de Tango":"13",
    "Paine":"13",
    "Melipilla":"13",
    "Alhué":"13",
    "Curacaví":"13",
    "María Pinto":"13",
    "San Pedro":"13",
    "Talagante":"13",
    "El Monte":"13",
    "Isla de Maipo":"13",
    "Padre Hurtado":"13",
    "Peñaflor":"13"
}

region_por_comuna = dict((normalize(k.lower()), v) for k,v in original_region_por_comuna.items())
