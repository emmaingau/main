import processing.net.*;
Server myServer;
PFont f;
String [] matrix = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"};

int i, q;  //Variables de indice para los for loops
int matrix_x=-10; 
int matrix_y=0;  //variables que necesitan valor inicial
String whatClientSaid = "joaquin";
String t, v, current;
String[] names = {"joaquin", "martin", "mateo", "belen", "ignacio"};

void setup(){
  f = loadFont("OCRAExtended-16.vlw");
  textMode(MODEL);
  myServer = new Server(this, 1243, "127.0.0.1");
  size(768, 1024);
  frameRate(60);
  
}

void draw(){
  Client thisClient = myServer.available();
  background(0);
  if(thisClient != null){
    whatClientSaid = thisClient.readString();  println(whatClientSaid);
    for(i=0; i<names.length; i++){
      if(whatClientSaid==names[i]){
        matrix(whatClientSaid);
      }
      else{
        background(#FFFFFF);
      }
    }
  }
}


void matrix(String v) {
  for (int q=0 ; q<matrix.length ; q++){
    current = matrix[(int)random(36)];
    textFont(f,16);                  
    fill(#42C920);
    text(current,matrix_x, matrix_y);
    if(matrix_y>650){
      matrix_x+=10;
      matrix_y=0;
      
    }
    if(matrix_x>650){
      matrix_x=0;
      matrix_y+=20;
      for (int u=0 ; u<names.length ; u++){
      if (v==names[u]){
        rect(230, 275, 200, 30);
        textFont(f, 26);
        fill(12);
        text(names[u], 250, 300);
      }
    }
    }
    else{
      matrix_y+=10;
    }
    
        
  }
}
