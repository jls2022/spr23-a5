all: calculator

calculator: main.o addition.o subtraction.o multiplication.o division.o 
	cc -o calculator main.o addition.o subtraction.o multiplication.o division.o 

main.o: main.c
	cc -c main.c

addition.o: addition.c
	cc -c addition.c

subtraction.o: subtraction.c
	cc -c subtraction.c

multiplication.o: multiplication.c
	cc -c multiplication.c

division.o: division.c
	cc -c division.c

clean:
	rm -rf *.o



	
