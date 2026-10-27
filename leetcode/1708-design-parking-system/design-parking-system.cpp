class ParkingSystem {
public:
    int c[3];
    ParkingSystem(int big, int medium, int small) {
        c[0] = big;
        c[1] = medium;
        c[2] = small;
    }
    
    bool addCar(int carType) {
        return c[carType-1]-- >0;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
    