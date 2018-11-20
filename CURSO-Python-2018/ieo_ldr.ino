/*
  www.diymakers.es
  by A.García & M.García
  Crear servidor Web con Arduino
  Tutorial en: http://diymakers.es/crear-servidor-web-con-arduino/
*/
 
#include <SPI.h>  //Importamos librería comunicación SPI
#include <Ethernet.h>  //Importamos librería Ethernet

//Ponemos la dirección MAC de la Ethernet Shield que está con una etiqueta debajo la placa 
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

//Asingamos la IP al Arduino
IPAddress ip(192,168,1,80); 
EthernetServer server(80); //Creamos un servidor Web con el puerto 80 que es el puerto HTTP por defecto
 
int led_ldr = 4; 	// Pin del relé activado por la ldr
int led_lan = 5; 	// Pin del relé activado por la lan
int sensorPin = A0; // Sensor de la LDR
int sensorValue = 0;// Valor de tensión leído
String estado="OFF";//Estado del Led inicialmente "OFF"
 
void setup(){
  Serial.begin(9600);
 
  // Inicializamos la comunicación Ethernet y el servidor
  Ethernet.begin(mac,ip);
  server.begin();
  Serial.print("Server is at ");
  Serial.println(Ethernet.localIP());
 
  pinMode(led_ldr,OUTPUT);
  pinMode(led_lan,OUTPUT);
  pinMode(13,OUTPUT);
}
 
void loop()
{
	/*
	char web[50];
	web="Esto es una prueba";
	*/
  
	// Creamos un cliente Web
	EthernetClient client = server.available(); 
  
	// Cuando detecte un cliente a través de una petición HTTP
	if (client){
		Serial.println("new client");
		// Una petición HTTP acaba con una línea en blanco
		boolean currentLineIsBlank = true; 
		// Creamos una cadena de caracteres vacía
		String cadena="";
		while(client.connected()){
			if(client.available()) {
				// Leemos la petición HTTP carácter por carácter
				char c = client.read();
				//Visualizamos la petición HTTP por el Monitor Serial
				Serial.write(c);
				// Unimos el String 'cadena' con la petición HTTP (c). 
				// De esta manera convertimos la petición HTTP a un String
				cadena.concat(c);
				 // Ya que hemos convertido la petición HTTP a una cadena de caracteres, 
				 // ahora podremos buscar partes del texto.
				 
				 //Guardamos la posición de la instancia "LED=" a la variable 'posicion'
				 int posicion=cadena.indexOf("LED="); 

				 //Si a la posición 'posicion' hay "LED=ON"
				  if  (cadena.substring(posicion)=="LED=ON"){
					digitalWrite(led_lan,HIGH);
					estado="ON";
				  }
				  //Si a la posición 'posicion' hay "LED=OFF"
				  if(cadena.substring(posicion)=="LED=OFF"){
					digitalWrite(led_lan,LOW);
					estado="OFF";
				  }

				// Cuando reciba una línea en blanco, 
				// quiere decir que la petición HTTP ha acabado y 
				// el servidor Web está listo para enviar una respuesta
				if (c == '\n' && currentLineIsBlank) {

					// Enviamos al cliente una respuesta HTTP
					client.println("HTTP/1.1 200 OK");
					client.println("Content-Type: text/html");
					client.println();

					//Página web en formato HTML
					client.println("<html>");
					client.println("<head>");
					client.println("<title>Arduino-IEO");
					client.println("</title>");
					client.println("</head>");
					client.println("<body>");
					client.println("<h1 align='center'>Arduino-IEO</h1>");
					client.println("<h3 align='center'>LED controlado por Servidor Web de Arduino</h3>");
					//client.println(web);
					
					//Creamos los botones. Para enviar parametres a trav�s de HTML se utiliza el metodo URL encode. Los par�metros se envian a trav�s del s�mbolo '?'
					client.println("<div style='text-align:center;'>");
					client.println("<button onClick=location.href='./?LED=ON\' style='margin:auto;background-color: #84B1FF;color: snow;padding: 10px;border: 1px solid #3F7CFF;width:65px;'>");
					client.println("ON");
					client.println("</button>");
					client.println("<button onClick=location.href='./?LED=OFF\' style='margin:auto;background-color: #84B1FF;color: snow;padding: 10px;border: 1px solid #3F7CFF;width:65px;'>");
					client.println("OFF");
					client.println("</button>");
					client.println("<br /><br />");
					client.println("<b>LED = ");
					client.print(estado);
					client.println("</b><br />");
					client.println("</b>");
					client.println("LDR: ");
					client.print(sensorValue);
					client.println("</body>");
					client.println("</html>");
					break;
				}
				if (c == '\n') {
				  currentLineIsBlank = true;
				}
				else if (c != '\r') {
				  currentLineIsBlank = false;
				}
			}
		}
		delay(1); 		// Da tiempo al navegador para recibir los datos
		client.stop();	// Cierra la conexión
	}
	sensorValue = analogRead(sensorPin);
	if(sensorValue<80){
		digitalWrite(led_ldr, HIGH);
		delay(500);
	}
	else{
		digitalWrite(led_ldr, LOW);
		delay(500);
	}
}
