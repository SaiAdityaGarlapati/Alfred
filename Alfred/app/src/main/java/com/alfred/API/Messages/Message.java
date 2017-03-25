package com.alfred.API.Messages;

/**
 * Created by manav on 17/3/17.
 */

public class Message {
    private String message;
    private boolean isSelf;

    public Message() {
    }

    public Message(String message, boolean isSelf) {
        this.message = message;
        this.isSelf = isSelf;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public boolean isSelf() {
        return isSelf;
    }

    public void setSelf(boolean self) {
        isSelf = self;
    }
}
