/*
 * HTTP Client POST Request
 * Copyright (c) 2018, circuits4you.com
 * All rights reserved.
 * https://circuits4you.com 
 * Connects to WiFi HotSpot. */

#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>

#include <WiFiUdp.h>


WiFiUDP Udp;
unsigned int localUdpPort = 4210;
char incomingPacket[256];
char replyPacket[] = "Hi there! Got the message :-)";


/* Set these to your desired credentials. */
const char *ssid = "freebox_SGPYLC";  //ENTER YOUR WIFI SETTINGS
const char *password = "";

//Web/Server address to read/write from 
const char *host = "192.168.0.38";   //https://circuits4you.com website or IP address of server



//=======================================================================
//                    Power on setup
//=======================================================================

void setup() {
  delay(1000);
  Serial.begin(9600);
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  
  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");

  Serial.print("Connecting");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP
}

//=======================================================================
//                    Main Program Loop
//=======================================================================
char  ReplyBuffer[10] = "";
void loop() {
  int adcvalue=analogRead(A0);
  //uint8_t buffer[50] = adcvalue;
  byte message[2];
  message[0] = 0;
  message[1] = 100000;  
  //String ADCData;
  //Read Analog value of LDR
  //char  ReplyBuffer[10] = String(adcvalue);
  Udp.begin(localUdpPort);
  Udp.beginPacket("192.168.0.38", 9999);
  Udp.write(itoa(adcvalue, ReplyBuffer, 10));
  Udp.endPacket();
  delay(10);
}
//=======================================================================
