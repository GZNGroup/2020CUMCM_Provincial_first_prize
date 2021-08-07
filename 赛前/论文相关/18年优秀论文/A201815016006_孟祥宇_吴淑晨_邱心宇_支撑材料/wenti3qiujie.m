clear;%�������������
clc;%����
close all;%�ر�����ͼ�δ���

%% ���ϲ�������
m1=6;m2=60;m3=36;m4=50;%�ֱ�����ֽ��ʷָ�
m=m1+m2+m3+m4;%���ʷָ��
n=1800;%��ʱ��ָ�
t=1800;%��ʱ��
h=8.6125;%��������ϵ��
l1=0.6/1000;l3=3.6/1000;% ���Ϻ��
lam_1=0.082;lam_2=0.37;lam_3=0.045;lam_4=0.028;% ���ֲ��ϵ��ȴ�����
de_1=300;de_2=862;de_3=74.2;de_4=1.18;% ���ֲ��ϵ��ܶ�
c1=1377;c2=2100;c3=1726;c4=1005;% ���ֲ��ϵı�����

%% ��������ɢ��
a1=lam_1/(c1*de_1);% I����ϵ�����ɢ��
a2=lam_2/(c2*de_2);% II����ϵ�����ɢ��
a3=lam_3/(c3*de_3);% III����ϵ�����ɢ��
a4=lam_4/(c4*de_4);% IV����ϵ�����ɢ��

optimum1=[];%�洢����II����ϵĳ���
optimum2=[];%�洢����IV����ϵĳ���
for l2=(0.6:0.1:25)/1000
    for l4=(0.6:0.1:6.4)/1000
   
%% ���ϳ��ȷָ��ʱ�䲽���ָ����
derta_x1=l1/m1;%I����ϵķָ��
derta_x2=l2/m2;%II����ϵķָ��
derta_x3=l3/m3;%III����ϵķָ��
derta_x4=l4/m4;%IV����ϵķָ��
derta_t=t/n;%ʱ�䲽���ָ�

%% �����������ʷֵĲ�����
r1=derta_t/derta_x1^2*a1;%��I������ʷֵĲ�����
r2=derta_t/derta_x2^2*a2;%��II������ʷֵĲ�����
r3=derta_t/derta_x3^2*a3;%��III������ʷֵĲ�����
r4=derta_t/derta_x4^2*a4;%��IV������ʷֵĲ�����


u=zeros(m+1,n+1);%�����Ĳ���Ͻ����¶ȷֲ�����
%% ��ʼ�����ͱ߽�����
u(1,:)=80;%�߽�����
u(:,1)=37;%��ʼ����

%% ��ָ�ʽ��ϵ������
A=zeros(m1+m2+m3+m4,m1+m2+m3+m4);
for i=1:m1-1
 A(i,i)=1+2*r1;
 A(i,i+1)=-r1;
if i>=2
A(i,i-1)=-r1;
end
end
A(m1,m1)=(lam_1/derta_x1+lam_2/derta_x2);
A(m1,m1-1)=-lam_1/derta_x1;
A(m1,m1+1)=-lam_2/derta_x2;

for i=m1+1:m1+m2-1
A(i,i)=1+2*r2;
 A(i,i+1)=-r2;    
A(i,i-1)=-r2;
end
A(m1+m2,m1+m2)=(lam_2/derta_x2+lam_3/derta_x3);
A(m1+m2,m1+m2-1)=-lam_2/derta_x2;
A(m1+m2,m1+m2+1)=-lam_3/derta_x3;

for i=m1+m2+1:m1+m2+m3-1
A(i,i)=1+2*r3;
 A(i,i+1)=-r3;    
A(i,i-1)=-r3;
end

A(m1+m2+m3,m1+m2+m3)=(lam_3/derta_x3+lam_4/derta_x4);
A(m1+m2+m3,m1+m2+m3-1)=-lam_3/derta_x3;
A(m1+m2+m3,m1+m2+m3+1)=-lam_4/derta_x4;

for i=m1+m2+m3+1:m1+m2+m3+m4-1
A(i,i)=1+2*r4;
A(i,i-1)=-r4;
 A(i,i+1)=-r4;    
end
A(m,m)=h+lam_4/derta_x4;
A(m,m-1)=-lam_4/derta_x4;

%% �����Ҷ���
for k=2:n+1
   
b=zeros(m,1);
for i=2:m-1
b(i,1)=u(i+1,k-1);
end
b(1,1)=u(2,k-1)+r1*u(1,k);
b(m1,1)=0;
b(m1+m2,1)=0;
b(m1+m2+m3,1)=0;
b(m,1)=37*h;

%% ׷�Ϸ���ⷽ��
bb=diag(A)';
aa=[0,diag(A,-1)'];
c=diag(A,1)';
N=length(bb);
L=zeros(N);
uu0=0;y0=0;aa(1)=0;
L(1)=bb(1)-aa(1)*uu0;
y(1)=(b(1)-y0*aa(1))/L(1);
uu(1)=c(1)/L(1);
for i=2:(N-1)
L(i)=bb(i)-aa(i)*uu(i-1);
y(i)=(b(i)-y(i-1)*aa(i))/L(i);
uu(i)=c(i)/L(i);
end
L(N)=bb(N)-aa(N)*uu(N-1);
y(N)=(b(N)-y(N-1)*aa(N))/L(N);
x(N)=y(N);
for i=(N-1):-1:1
x(i)=y(i)-uu(i)*x(i+1);
end
u(2:m+1,k)=x';

end
if u(m+1,1800)<=47&u(m+1,1501)<=44%��������
    optimum1=[optimum1 l2*1000];
    optimum2=[optimum2 l4*1000];
end
    end
end

q=optimum1+optimum2;
[p e]=min(optimum1);
fprintf('l2��С�ɱ����ʱ����II������IV���ܺ�ȣ�\n')
fprintf('   12=%.1f\n',optimum1(e))
fprintf('   14=%.1f\n',optimum2(e))
fprintf('   12+l4=%.1f\n\n',q(e))

fprintf('l2+l4��С�����Сʱ����II������IV���ܺ�ȣ�\n')
fprintf('  12=%.1f   %.1f\n',optimum1(1),optimum1(2))
fprintf('  14=%.1f   %.1f\n',optimum2(1),optimum2(2))
fprintf('  12+l4=%.1f  %.1f\n',q(1),q(2))


