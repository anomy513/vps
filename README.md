# VPS - Sistema de comunicación cifrada

## Idea del proyecto

La idea de este proyecto es crear un sistema de comunicación capaz de enviar
mensajes y archivos de un equipo a otro de forma cifrada.

El objetivo es que la información que viaje por la red no pueda ser leída
directamente. El mensaje o archivo será transformado mediante un proceso
matemático de cifrado y solamente el equipo que tenga la clave correspondiente
podrá recuperar la información original.

Por ejemplo:

    Mensaje original
          ↓
       Cifrado
          ↓
    Datos ilegibles
          ↓
       Red / VPS
          ↓
      Descifrado
          ↓
    Mensaje original

El sistema también deberá poder trabajar con archivos y documentos, no
solamente con mensajes de texto.

## Objetivos

- Crear un sistema de cifrado y descifrado.
- Poder cifrar mensajes de texto.
- Poder cifrar archivos y documentos.
- Poder enviar información cifrada a través de una red.
- Utilizar un VPS como parte de la comunicación.
- Mantener las claves privadas protegidas.
- Evitar que el servidor tenga que conocer el contenido de los mensajes.
- Documentar el desarrollo y las pruebas del proyecto.

## Desarrollo

El proyecto comenzará como una prueba local para entender cómo funcionan
el cifrado, las claves y el descifrado.

Después se añadirá la comunicación entre equipos y finalmente la utilización
del VPS como intermediario.

## Seguridad

La intención es utilizar algoritmos criptográficos conocidos y seguros en
lugar de crear un algoritmo criptográfico propio para proteger información
real.

Las claves privadas no deberán almacenarse ni publicarse dentro del
repositorio.

## Estado

Proyecto en desarrollo.

Este repositorio irá creciendo conforme avance el desarrollo y se documenten
las diferentes pruebas y soluciones.
