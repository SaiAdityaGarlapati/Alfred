package com.alfred.API.Contacts;

/**
 * Created by manav on 25/3/17.
 */

public interface ContactCallback {

    void getContact(ContactImpl contact);

    void contactSaveStatus(boolean saved);
}
