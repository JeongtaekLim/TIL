# GenericAPIView

This class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

DRF의 APIView 클래스를 상속하는 클래스로, 표준형 list와 detail view를 구현하는데 사용됩니다.

Each of the concrete generic views provided is built by combining GenericAPIView, with one or more mixin classes.

실제 generic view들은 주로 GenericAPIView들과, 하나 또는 그 이상의 클래스들을 조합하여 만들어진다.
(중요한 대목입니다. 오늘은 이걸 하나 건져가네요)