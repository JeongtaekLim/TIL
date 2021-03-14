# Network 기초

- IP 주소는 32자리 2진수로 표현됨
- 네트워크 영역(192.168.0.0)과 호스트영역(192.168.0.3, 192.168.0.4, ...) 등으로 구분됨
- 192.168.0.1/24 => 1111.1111.1111.1111.1111.1111.0000.0000 => 255.255.255.255.0

# AWS 네트워크 기초

- AWS 네트워크는 VPC라는 단위로 구성되어 있음. [AWS docs 참고](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html)
- 1개의 VPC는 1개 Region에 위치함
- 1개의 VPC는 여러개 가용영역에 걸쳐 구성될 수 있음
- 1개의 VPC는 여러개 서브넷으로 구성됨

# AWS EC2 with custom VPC

- AWS 계정 생성 당시 기본으로 부여된 VPC 이외에 custom VPC를 생성하는 경우 체크해야할 점이 몇가지 있음
- Public IP가 EC2 인스턴스에 잘 부여되어 있는지
- EC2 인스턴스가 public subnet에 포함되어 있고, 그 public subnet은 Internet Gateway를 가리키는 Route Table을 가지고 있는지
- EC2 인스턴스의 보안그룹이 ssh 포트에 대한 적절한 inbound 규칙을 가지고 있는지

내 경우, EC2 인스턴스가 public subnet에 포함되어 있었지만, 그 public subnet이 Internet Gateway를 가리키는 Route Table을 가지고 있지 않았다.
따라서, Internet Gateway를 생성하고 Route Table에 추가함으로써 문제를 해결함(이때, 기존의 default VPC의 설정을 참고하면 도움이 됨)
