import processing.net.*;
Server myServer;
PFont f;
String [] matrix = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"};
String [] names = {"AARON", "ABEL", "ABELARDO", "ABRAHAM", "ADALBERTO", "ADAN","ADOLFO", "ADRIAN","AGUSTIN","ALAN","ALBERTO","ALDO","ALEJANDRO","ALFONSO","ALFREDO","ALONSO","ALVARO","AMADO","ANDRES","ANGEL","ANSELMO","ANTONIO","APOLINAR","ARIEL","ARISTEO","ARMANDO","ARNOLDO","ARNULFO","ARTEMIO","ARTURO","AUGUSTO","AURELIANO","AURELIO","BALTAZAR","BEATRIZ","BELÉN","BENITO","BENJAMIN","BERNABE","BERNARDINO","BERNARDO","CANDELARIO","CANDIDO","CARLOS","CARMEN","CECILIO","CESAR","CHRISTIAN","CIRILO","CLAUDIO","CLEMENTE","CONCEPCION","CONSTANTINO","CRISTIAN","CRISTOBAL","CRUZ","CUAUHTEMOC","DAGOBERTO","DAMIAN","DANIEL","DARIO","DAVID","DELFINO","DEMETRIO","DIEGO","DOMINGO","EDGAR","EDGARDO","EDMUNDO","EDUARDO","EDWIN","EFRAIN","EFREN","ELEAZAR","ELIAS","ELIGIO","ELISEO",
"ELOY","EMILIANO","EMILIO","EMMA","EMA","EMMANUEL","ENRIQUE","ERASMO","ERIC","ERICK","ERIK","ERNESTO","ESTEBAN","EUGENIO","EUSEBIO","EVARISTO","EVERARDO","EZEQUIEL","FABIAN","FAUSTINO","FAUSTO","FEDERICO","FELICIANO","FELIPE","FELIPE DE JESUS","FELIX","FERMIN","FERNANDO","FIDEL","FILIBERTO","FLORENCIO","FLORENTINO","FORTINO","FRANCISCO","FREDY","GABINO","GABRIEL","GAMALIEL","GASTÓN","GENARO","GERARDO","GERMAN","GILBERTO","GILDARDO","GONZALO","GREGORIO","GUADALUPE","GUILLERMO","GUSTAVO","HECTOR","HERIBERTO","HERNAN","HILARIO","HIPOLITO","HOMERO","HORACIO","HUGO","HUMBERTO","IGNACIO","NACHO","ISAAC","ISABEL","ISAIAS","ISIDRO","ISMAEL","ISRAEL","IVAN","JACINTO","JACOBO","JAIME","JAVIER","JERONIMO","JESUS","JOAQUIN","JOEL","JONATHAN","JORGE","JOSE","JOSE DE JESUS","JOSUE","JUAN","JUAN DE DIOS",
"JULIAN","JULIO","JUSTINO","JUVENTINO","LAZARO","LENIN","LEOBARDO","LEONARDO","LEONEL","LEOPOLDO","LORENZO","LUCIANO","LUCIO","LUIS","MANUEL","MANUEL DE JESUS","MARCELINO","MARCELO","MARCO","MARCOS","MARGARITO","MARIA","MARIANO","MARIO","MARTIN","MATEO","MAURICIO","MAURO","MAXIMINO","MAXIMO","MIGUEL","MILTON","MISAEL","MODESTO","MOISES","NESTOR","NICOLAS","NOE","NOEL","NORBERTO","OCTAVIO","OMAR","ORLANDO","OSCAR","OSVALDO","OSWALDO","PABLO","PASCUAL","PATRICIO","PEDRO","PORFIRIO","RAFAEL","RAMIRO","RAMON","RAUL","RAYMUNDO","REFUGIO","RENE","REY","REYES","REYNALDO","RICARDO","RIGOBERTO","ROBERTO","RODOLFO","RODRIGO","ROGELIO","ROGER","ROLANDO","ROMAN","ROSALIO","ROSARIO","ROSENDO","RUBEN","SABINO","SALOMON","SALVADOR","SAMUEL","SANTIAGO","SANTOS","SAUL","SEBASTIAN","SERGIO","SILVESTRE","SIMON","TEODORO","TOMAS","TRINIDAD",
"UBALDO","ULISES","URIEL","VALENTIN","VALENTINA","VICENTE","VICTOR","VICTORIA","VIRGILIO","VLADIMIR","WILBERT"};

int x = -10;
int y = 0;
String whatClientSaid; // variable que venga de python
String joaco = "JOAQUIN";

void setup(){
  myServer = new Server(this, 1243, "127.0.0.1");
  frameRate(30);
  background(12);
  size(600, 600);
  smooth();
  f = loadFont("OCRAExtended-16.vlw");
  textMode(MODEL);
}

void draw(){
  Client thisClient = myServer.available();
  if (thisClient !=null) {
    whatClientSaid = thisClient.readString();
    println(whatClientSaid);
    for (int n=0;n<names.length;n++){
      if ((String)whatClientSaid==joaco){
        println("matrixforever");
      }
      else{
        background(#FFFFFF);
      }
    }
  }
  
}

void matrix(String var) {
  for (int i=0 ; i<matrix.length ; i++){
    String current = matrix[(int)random(36)];
    textFont(f,16);                  
    fill(#42C920);
    text(current,x, y);
    if(y>650){
      x+=10;
      y=0;
      
    }
    if(x>650){
      x=0;
      y+=20;
      theChosenOne(var);
    }
    else{
      y+=10;
    }
    
        
  }
}

void theChosenOne(String var2){
  for (int username=0 ; username<names.length ; username++){
      if (var2==names[username]){
        rect(230, 275, 200, 30);
        textFont(f, 26);
        fill(12);
        text(names[username], 250, 300);
      }
    }
}
