package com.alfred.API.Location;

import android.location.Location;

/**
 * Created by manav on 22/3/17.
 */

public interface LocationCallback {

    void updateLocation(Location location);

    void updateAddress(String address);
}
