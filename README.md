ใน folder project จะมี 2 file และ 2 folder

1. network.sql คือ file database นำไฟล์นี้ไป import ใน phpmyadmin และตั้งชื่อ database ให้ตรงกับใน file อื่นๆ

2. README.md คือ file นี้

3. mqtt-app folder จะมีไฟล์อยู่อีกหลายไฟล์ แต่ไฟล์ที่ใช้/สนใจ จะมี
    - SampleInput.xlsx คือไฟล์ข้อมูลที่ publisher ใช้ในการส่งข้อมูลไปยัง broker
    - publish.py และ publish2.py คือไฟล์ publisher ที่จะส่งข้อมูลที่อ่านจาก SampleInput.xlsx ไปยัง broker ตาม topic ที่ได้เขียนไว้
    - subscribe.py คือไฟล์ที่จะส่ง topic ที่สนใจไปที่ broker เมื่อ broker ได้ topic ที่ตรงกันกับที่ subscribe ไว้ก็จะส่ง data มายัง subscribe.py หลังจากนั้นก็จะส่งข้อมูลที่ได้บันทึกเข้า database
    - query.py ใช้สำหรับดึงข้อมูลจาก database ออกมาแสดงผลใน command (command base)

4. web folder จะไฟล์อยู่อีกหลายไฟล์หลาย folder แต่ไฟล์ที่ใช้/สนใจ จะมี
    - /src/api.js file นี้จะเป็น file ที่เชื่อม database และนำข้อมูลมาทำเป็น api เพื่อนำไปใช้ต่อไป
    - /src/index.html file นี้จะเป็น file ที่จะนำข้อมูลจากการ fetch api ไปแสดงบน website




วิธีการใช้งาน 
1. สร้าง database ชื่อเดียวกับใน code และเปิดขึ้นมา
2. install python, node และทุกอย่างที่จำเป็น
3. run file subscribe.py และ publisher.py
4. run query.py เพื่อดูข้อมูลใน database
5. run api.js และเปิดเว็บ index.html เพื่อดูข้อมูลใน database แบบบนเว็บไซท์