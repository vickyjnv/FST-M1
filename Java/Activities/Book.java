package activities;


    abstract class Book {
        String title;
        //Abstract method
        abstract void setTitle(String s);

        //Concrete method
        String getTitle() {
            return title;
        }
    }

