import processing.net.*;
PImage colors;
PImage sports;
PImage occupations;
Server myServer;
int orden;

// VARIABLES DEPORTES
int xd;
int yd;
int ixd; // variable para cambios de dirección en x
int iyd; // variable para cambios de dirección en y

// VARIABLES OCUPACIONES

String loadOccupation;
int imageOn;
int xo;
int yo;
int ixo;
int iyo;


// VARIABLES COLORES
int r;
int g;
int b;

//StringLists varias

StringList colores;
StringList rgbList;
int rgbIndex;
String rgbChosen;
StringList deportes;
StringList ocupaciones;



void setup(){
  
  
  // RELACIONADO CON SOCKETS
  myServer = new Server(this, 1243, "127.0.0.1");
  
  // CONTADOR DE ÍNDICE -para los colores que son dos listas-
  
  
  size(500,500);
  frameRate(60);
  
  // CARGA DE AVATARES -Esto tiene toda la pinta que se va al draw() para poder cambiarlos según respuesta- 
  sports = loadImage("sports.png");
  colors = loadImage("colors.png");
  
  // POS INICIAL Y DIRECCIÓN -DEPORTES-
  xd = 1000;
  yd = 1000;  
  ixd = 1;
  iyd = 1;
  
  // POS INICIAL, DIRECCIÓN E INVOCACIÓN -OCUPACIONES-
  xo = 1000;
  yo = 1000;  
  ixo = 2;
  iyo = 2;
  imageOn = 0;
  
  // fondo
  
 /* r = 200;
  g = 0;
  b = 200;
  */
  
  // COLORES SIMPLES
  
  colores = new StringList();
  colores.append("negro");
  colores.append("blanco");
  colores.append("rojo");
  colores.append("verde");
  colores.append("azul");
  colores.append("fucsia");
  
  // ASOCIACIÓN RGB A COLORES SIMPLES
  
  rgbList = new StringList();
  rgbList.append("0,0,0");
  rgbList.append("255,255,255");
  rgbList.append("255,0,0");
  rgbList.append("0,255,0");
  rgbList.append("0,0,255");
  rgbList.append("200,0,200");
  
  
  
  /*
  // COLORES
  colores = new StringList();
  colores.append("verde");
  colores.append("amarillo");
  colores.append("violeta");
  colores.append("rojo");
  colores.append("azul");
  colores.append("blanco");
  colores.append("gris");
  colores.append("celeste");
  colores.append("lila");
  colores.append("magenta");
  colores.append("negro");
  colores.append("naranja");
  colores.append("marrón");
  colores.append("beige");
  colores.append("mostaza");
  colores.append("rosado");
  colores.append("rosa");
  colores.append("salmón");
  colores.append("turquesa");
  colores.append("verde agua");
  colores.append("cian");
  colores.append("terracota");
  
  */
  // DEPORTES
  deportes = new StringList();
  deportes.append("Tenis");
  deportes.append("Rugby");
  deportes.append("badminton");
  deportes.append("balonmano");
  deportes.append("basquetbol");
  deportes.append("fútbol");
  deportes.append("beisbol");
  deportes.append("processing");
  deportes.append("cricket");
  deportes.append("hockey");
  
  // OCUPACIONES
  
  ocupaciones = new StringList();
  ocupaciones.append("trabajo");
  ocupaciones.append("estudio");
  
}

void draw(){
  Client thisClient = myServer.available();
  // Recarga del fondo, lo que permite que se vea la imagen
  background(r,g,b);
  
  // Carga de avatares en el Draw
  image(sports, xd, yd);
  if(imageOn == 1){
    image(occupations, xo, yo);
  }
  // ANIMACIONES AVATARES
  // Deportes
  xd+=ixd;
  yd+=iyd;
  
  if (xd == 300 || xd == -10){
    ixd = ixd*(-1);
  }
  if (yd == 300 || yd == -10){
    iyd = iyd*(-1);
  }
  
  // Ocupaciones
  xo+=ixo;
  yo+=iyo;
  
  if (xo == 300 || xo == -10){
    ixo = ixo*(-1);
  }
  if (yo == 300 || yo == -10){
    iyo = iyo*(-1);
  }
  
  //println(yo); // debug
  
  if (thisClient !=null) {
    String whatClientSaid = thisClient.readString();
    println(whatClientSaid);
    if(colores.hasValue(whatClientSaid)){
      rgbIndex = colores.index(whatClientSaid);
      rgbChosen = rgbList.get(rgbIndex);
      String[] rgbSplit = split(rgbChosen, ',');
      r = int(rgbSplit[0]);
      g = int(rgbSplit[1]);
      b = int(rgbSplit[2]);
      // background(r,g,b);
    }
    if(deportes.hasValue(whatClientSaid)){
      xd = 0;
      yd = 0;
      // background(r,g,b);
    }
    if(ocupaciones.hasValue(whatClientSaid)){
      loadOccupation = (whatClientSaid + ".png");
      occupations = loadImage(loadOccupation);
      xo = 0;
      yo = 0;
      imageOn = 1;
  }
}
}
