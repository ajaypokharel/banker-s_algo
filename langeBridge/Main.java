package langeBridge;

import java.lang.Thread;

import java.util.Random;

public class Main {

    final private static int FARMERS = 6;

    public static void main(String[] args) {

        Bridge laneBridge = new Bridge();

        Random r = new Random();

        System.out.println(FARMERS + " farmers try to enter the bridge");

        for (int i = 0; i < FARMERS; i++) {

            Farmer farmer;

            if (r.nextBoolean()) {

                farmer = new SouthBoundFarmer(laneBridge);

            } else {

                farmer = new NorthBoundFarmer(laneBridge);

            }

            crossLane(farmer);

        }

    }

    private static void crossLane(Farmer f) {
        // start the farmer thread
        new Thread(f).start();

    }

}
