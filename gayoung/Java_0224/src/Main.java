import java.util.ArrayList;
import java.util.List;

public class Main {

  public static void main(String[] args) {
    int a;
    // int a= new A().getA();
    a = new A(1).getA();
    System.out.println(new A());
  }

}
class A{
  int a;
  public A(){}
  public A(int a){ this.a = a; }

  int getA(){
    return a;
  }
  @Override
  public String toString(){
   return "A class 입니다.";
  }
}