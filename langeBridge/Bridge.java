package langeBridge;

import java.lang.InterruptedException;

import java.util.concurrent.Semaphore;

public class Bridge {

    private Semaphore lock;

    public Bridge() {

        this.lock = new Semaphore(1);

    }

    public void enterLane() throws InterruptedException {

        this.lock.acquire();

    }

    public void leaveLane() {

        this.lock.release();

    }

}