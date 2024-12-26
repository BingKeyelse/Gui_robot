/* File hoàn chỉnh cho 5 khớp chạy */

#include <TimerOne.h>

#define DIR_1 3
#define PULSE_1 4


#define servoPin 9
//==============================================================
//==============================================================

volatile int count_1, xung_com_1, error_1;
volatile float vitri_1, vitri_dat_1;
volatile float vitri_thuc_1;
volatile int T1;

volatile float the_1, the_1_pre, the_1_flex;
volatile float a1, b1, c1, d1;
volatile float t_count, t_command, t_quyhoach_1;

//==============================================================
//==============================================================
volatile float vitri_dat_6,vitri_thuc_6;
int x6;
//==============================================================
//==============================================================

void setup()
{
  //==============================================================
  //==============================================================
  pinMode(DIR_1, OUTPUT); // CHAN PWM
  pinMode(PULSE_1, OUTPUT); //chan dieu khien dong co
  digitalWrite(PULSE_1, LOW);
  //===============================
  vitri_dat_1 = 0;
  vitri_1 = 0;
  vitri_thuc_1 = vitri_1;
  xung_com_1 = 0;
  count_1 = 0;
  T1 = 8;
  t_count = 0;
  t_command = 0;
  t_quyhoach_1 = 0;
  error_1 = 0;
  
  //==============================================================
  //==============================================================

  //==============================================================
  //==============================================================
  Serial.begin(115200); //khoi tao gui thong tin serial
  Timer1.attachInterrupt(dieu_khien_1);
}

void phat_xung(unsigned int chan_phat_xung, unsigned int timedl)
{
  digitalWrite(chan_phat_xung, HIGH);
  delayMicroseconds(timedl);
  digitalWrite(chan_phat_xung, LOW);
  delayMicroseconds(timedl);
}

void forward(unsigned int chan_chieu)
{
  digitalWrite(chan_chieu, HIGH);
}

void reverse(unsigned int chan_chieu)
{
  digitalWrite(chan_chieu, LOW);
}

void Stop(unsigned int chan_chieu, unsigned int chan_phat_xung)
{
  digitalWrite(chan_chieu, LOW);
  digitalWrite(chan_phat_xung, LOW);
}

void dieu_khien_1()
{
  if ((the_1_flex - the_1_pre) > 0)
  {
    if (count_1 < round(the_1_flex - the_1_pre))
    {
      forward(DIR_1);
      phat_xung(PULSE_1, T1);
      count_1++;
      vitri_thuc_1 = vitri_thuc_1 + 0.01;
    }
    else
    {
      Stop(DIR_1, PULSE_1);
      Timer1.stop();
    }
  }
  else if ((the_1_flex - the_1_pre) < 0)
  {
    if (count_1 < abs(round(the_1_flex - the_1_pre)))
    {
      reverse(DIR_1);
      phat_xung(PULSE_1, T1);
      count_1++;
      vitri_thuc_1 = vitri_thuc_1 - 0.01;
    }
    else
    {
      Stop(DIR_1, PULSE_1);
      Timer1.stop();
    }
  }
  if (t_count > (t_command))
  {
    offset_1();
  }
}

void offset_1()
{
  error_1 = int((vitri_dat_1 - vitri_thuc_1) * 100);
  if (error_1 > 0)
  {
    forward(DIR_1);
    phat_xung(PULSE_1, T1);
    vitri_thuc_1 = vitri_thuc_1 + 0.01;
  }
  else if (error_1 < 0)
  {
    reverse(DIR_1);
    phat_xung(PULSE_1, T1);
    vitri_thuc_1 = vitri_thuc_1 - 0.01;
  }
}

void serialEvent()
{
  String test1 = "";
  String test2 = "";
  String test3 = "";
  String test4 = "";
  String test5 = "";
  String test6 = "";
  String test7 = "";
  if (Serial.available() > 0)
  {
    //thay bằng lệnh parseFloat
    test1 = Serial.readStringUntil(',');
    test2 = Serial.readStringUntil(',');
    test3 = Serial.readStringUntil(',');
    test4 = Serial.readStringUntil(',');
    test5 = Serial.readStringUntil(',');
    test6 = Serial.readStringUntil(',');
    test7 = Serial.readStringUntil('\n');

    vitri_dat_1 = test1.toFloat();    //Goc quay mong muon
    vitri_dat_2 = test2.toFloat();
    vitri_dat_3 = test3.toFloat();
    vitri_dat_4 = test4.toFloat();
    vitri_dat_5 = test5.toFloat();
    vitri_dat_6 = test6.toFloat();
    t_command = test7.toFloat();    // Thoi gian di chuyen mong muon

    if ((vitri_dat_1<-90) || (vitri_dat_1>90))    vitri_dat_1 = vitri_thuc_1;
    xung_com_1 = int((vitri_dat_1 - vitri_thuc_1) * 100);
    the_1 = xung_com_1;

    vitri_dat_6=round(vitri_dat_6);
    /* ---- Reset thoi gian bat dau qui hoach quy dao khop 1-----*/
    t_count = 0;
    the_1_pre = 0;
    the_1_flex = 0;
    count_1 = 0;

    a1 = the_1_pre;
    b1 = 0;
    c1 = 3 * (the_1 - the_1_pre) / (t_command * t_command);
    d1 = -2 * (the_1 - the_1_pre) / (t_command * t_command * t_command);
    /* ---- Ket thuc ceset thoi gian bat dau qui hoach quy dao-----*/

    /* ---- Reset thoi gian bat dau qui hoach quy dao khop 2-----*/
    t_count = 0;
    the_2_pre = 0;
    the_2_flex = 0;
    count_2 = 0;

    a2 = the_2_pre;
    b2 = 0;
    c2 = 3 * (the_2 - the_2_pre) / (t_command * t_command);
    d2 = -2 * (the_2 - the_2_pre) / (t_command * t_command * t_command);
    /* ---- Ket thuc ceset thoi gian bat dau qui hoach quy dao-----*/

    /* ---- Reset thoi gian bat dau qui hoach quy dao khop 3-----*/
    t_count = 0;
    the_3_pre = 0;
    the_3_flex = 0;
    count_3 = 0;

    a3 = the_3_pre;
    b3 = 0;
    c3 = 3 * (the_3 - the_3_pre) / (t_command * t_command);
    d3 = -2 * (the_3 - the_3_pre) / (t_command * t_command * t_command);
    /* ---- Ket thuc ceset thoi gian bat dau qui hoach quy dao-----*/

    /* ---- Reset thoi gian bat dau qui hoach quy dao khop 4-----*/
    t_count = 0;
    the_4_pre = 0;
    the_4_flex = 0;
    count_4 = 0;

    a4 = the_4_pre;
    b4 = 0;
    c4 = 3 * (the_4 - the_4_pre) / (t_command * t_command);
    d4 = -2 * (the_4 - the_4_pre) / (t_command * t_command * t_command);
    /* ---- Ket thuc ceset thoi gian bat dau qui hoach quy dao-----*/

    /* ---- Reset thoi gian bat dau qui hoach quy dao khop 5-----*/
    t_count = 0;
    the_5_pre = 0;
    the_5_flex = 0;
    count_5 = 0;

    a5 = the_5_pre;
    b5 = 0;
    c5 = 3 * (the_5 - the_5_pre) / (t_command * t_command);
    d5 = -2 * (the_5 - the_5_pre) / (t_command * t_command * t_command);
    /* ---- Ket thuc ceset thoi gian bat dau qui hoach quy dao-----*/

    Timer6.start(10000);  // Kich hoach qui hoach quy dao
  }
}

void quy_hoach() // Chuong trinh phuc vu ngat cho Timer 6 (10ms)
{
  //  t_count = t_count + 0.01;     // Tang thoi gian dem (buoc 10ms)
  the_1_pre = the_1_flex;           //Luu gia tri truoc

  if (t_count < t_command)
  {
    t_count = t_count + 0.01;     // Tang thoi gian dem (buoc 10ms)
    /*=============================================================================================================================*/
    the_1_flex = a1 + b1 * t_count + c1 * (t_count * t_count) + d1 * (t_count * t_count * t_count); // Quy hoach quy dao
    count_1 = 0;        // Reset so xung da goi
    if ((the_1_flex - the_1_pre) == 0)    t_quyhoach_1 = 10000;
    else t_quyhoach_1 = round(abs(5000 / (the_1_flex - the_1_pre)));
//    Timer1.start(t_quyhoach_1);

    /*=============================================================================================================================*/
    Timer1.start(t_quyhoach_1);
  }

  if (t_count > (t_command))
  {
//        Timer6.stop();
  }
}

void serial_full()
{
  if (Serial.availableForWrite() > 20)
  {
    Serial.print(vitri_dat_1);
    Serial.print(" === ");
    Serial.print(vitri_thuc_1);
    Serial.print(" === ");
    Serial.print(the_1_flex);
    Serial.print(" === ");
    Serial.print(the_1_pre);
    Serial.print(" === ");
    Serial.print(" === ");
    Serial.print(vitri_dat_2);
    Serial.print(vitri_thuc_2);
    Serial.print(" === ");
    Serial.print(the_2_flex);
    Serial.print(" === ");
    Serial.print(the_2_pre);
    Serial.print(" === ");
    Serial.print(vitri_dat_3);
    Serial.print(" === ");
    Serial.print(vitri_thuc_3);
    Serial.print(" === ");
    Serial.print(the_3_flex);
    Serial.print(" === ");
    Serial.print(the_3_pre);
    Serial.print(" === ");
    Serial.print(vitri_dat_4);
    Serial.print(" === ");
    Serial.print(vitri_thuc_4);
    Serial.print(" === ");
    Serial.print(the_4_flex);
    Serial.print(" === ");
    Serial.print(the_4_pre);
    Serial.print(" === ");
    Serial.print(vitri_dat_5);
    Serial.print(" === ");
    Serial.print(vitri_thuc_5);
    Serial.print(" === ");
    Serial.print(the_5_flex);
    Serial.print(" === ");
    Serial.print(the_5_pre);
    Serial.print(" === ");
    Serial.print(t_count);
    Serial.print(" === ");
    Serial.println(t_command);
  }
}

void serial_quan_sat()
{
  if (Serial.availableForWrite() > 20)
  {
    Serial.print(vitri_dat_1);
    Serial.print(" === ");
    Serial.print(vitri_thuc_1);
    Serial.print(" === ");
    Serial.print(vitri_dat_2);
    Serial.print(" === ");
    Serial.print(vitri_thuc_2);
    Serial.print(" === ");
    Serial.print(vitri_dat_3);
    Serial.print(" === ");
    Serial.print(vitri_thuc_3);
    Serial.print(" === ");
    Serial.print(vitri_dat_4);
    Serial.print(" === ");
    Serial.print(vitri_thuc_4);
    Serial.print(" === ");
    Serial.print(vitri_dat_5);
    Serial.print(" === ");
    Serial.print(vitri_thuc_5);    
    Serial.print(" === ");
    Serial.println(vitri_thuc_6);
  }
}

void serial_C_sharp()
{
  delay(50);
  if (Serial.availableForWrite() > 20)
  {
    Serial.print(vitri_thuc_1);
    Serial.print(",");
    Serial.print(vitri_thuc_2);
    Serial.print(",");
    Serial.print(vitri_thuc_3);
  }
}

void loop()
{
  dk_servo6();
  serial_C_sharp();   //Goi du lieu len C sharp , chỗ này mình sẽ dùng để gửi dữ liệu 
}