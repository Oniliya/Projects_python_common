class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2) # Вывод: True



# public class Singleton {
#     private static Singleton _instance = null;

#     private Singleton() {
#     // Приватный конструктор, чтобы предотвратить создание через new
# }

# public static Singleton getInstance() {
#     if (_instance == null) {
#         _instance = new Singleton();
#     }
#     return _instance;
# }

# public static void main(String[] args) {
#     Singleton singleton1 = Singleton.getInstance();
#     Singleton singleton2 = Singleton.getInstance();

#     // Проверяем, что объекты ссылаются на один и тот же экземпляр
#     System.out.println(singleton1 == singleton2); // Вывод: true
# }
# }