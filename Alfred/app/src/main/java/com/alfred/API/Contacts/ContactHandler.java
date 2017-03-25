package com.alfred.API.Contacts;

import android.app.Activity;
import android.content.Context;

import java.util.ArrayList;

/**
 * Created by manav on 25/3/17.
 */

public class ContactHandler {

    private Context context;
    private Activity activity;
    private ContactCallback callback;
    private ArrayList<ContactImpl> contactsList;

    public ContactHandler(Context context, Activity activity, ContactCallback callback) {
        this.context = context;
        this.activity = activity;
        this.callback = callback;

    }

    private ArrayList<ContactImpl> fetchList() {
        return null;
    }

    private void sendContact(ContactImpl contact) {
        callback.getContact(contact);
    }

    public void sendContactSavedStatus(boolean saved) {
        callback.contactSaveStatus(saved);
    }
}
