using System;
class Program {
  static void Main() {
    int len = 0x23;
    Console.Write("INPUT > ");
    string flag = Console.ReadLine();
    if ((flag.Length) != len) {
      Console.WriteLine("WRONG!");
    } else {
      if (flag[0] == 0x63 && flag[1] == 0x74 && flag[2] == 0x66 &&
          flag[3] == 0x34 && flag[4] == 0x62 && flag[5] == 0x7b &&
          flag[6] == 0x31 && flag[7] == 0x5f && flag[8] == 0x31 &&
          flag[9] == 0x69 && flag[10] == 0x6e && flag[11] == 0x33 &&
          flag[12] == 0x72 && flag[13] == 0x35 && flag[14] == 0x5f &&
          flag[15] == 0x6d && flag[16] == 0x61 && flag[17] == 0x6b &&
          flag[18] == 0x33 && flag[19] == 0x5f && flag[20] == 0x50 &&
          flag[21] == 0x47 && flag[22] == 0x5f && flag[23] == 0x68 &&
          flag[24] == 0x61 && flag[25] == 0x72 && flag[26] == 0x64 &&
          flag[27] == 0x5f && flag[28] == 0x32 && flag[29] == 0x5f &&
          flag[30] == 0x72 && flag[31] == 0x33 && flag[32] == 0x61 &&
          flag[33] == 0x64 && flag[34] == 0x7d) {
        Console.WriteLine("YES!!!\nThis is Flag :)");
      } else {
        Console.WriteLine("WRONG!");
      }
    }
  }
}