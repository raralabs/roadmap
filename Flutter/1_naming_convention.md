# Naming Convention

## Section 1 : Files and Folders

<br>

## How to name files and folders

You will use snake case for naming files and folders.<br>
Suppose, you want to create a folder with name "Sushan Shakya".<br> Here's how you name it : 

    |- sushan_shakya
    |  | - ...(other files inside folder)

Suppose, you want to create a file with name "Bottom Navigation".<br> Here's how you name it :

    |- some_folder
    |  |- bottom_navigation.dart

<br>

## Deciding filenames

### Screens

When you're creating a file for some "screen" in the app then you will always use `_view` as a suffix.<br>

Say, you want to create a file for "Home Screen".<br>
Your filename should be :

    |- some_folder
    |  |- home_view.dart


### Components

When you're creating a file for some component in the app then you will always use `_widget` as a suffix.<br>

Say, you want to create a file for "Bottom Navigation Button Component".<br>
Your filename should be :

    |- some_folder
    |  |- bottom_navigation_button_widget.dart


### Fragments

When you're creating a file for separating a small part of a screen with many components and some logic in the app then you will always use `_fragment` as a suffix.<br>

Say, you have a home screen which contains a listing widget then you can separate it from homeview into it's own component called as "Home View Listing Fragment".<br>
Your filename should be :

    |- some_folder
    |  |- home_view_listing_fragment.dart

### Models

Our app can have different types of model based on what our app is doing. The basic types of models are `App models` and `API models`. ( Ask a Senior Dev. in the team about it to learn more )<br><br>

But Basically the idea is that your app will have data classes which you'll create to work with any kind of data. Then you'll use `_model` as a suffix.<br>

Suppose that creating a data class for an API response. Let the response be for "User profile".<br>
Your filename should be :

    |- some_folder
    |  |- user_profile_response_model.dart

<br>
<hr>
<br>

## Section 2 : Classes and Mixins

<br>

## How to name classes and mixins

You will use "Upper Camel Case" for naming classes and mixins.<br> 

Supppose, you want to create a class for "Home Screen".<br>
Here's how you name it :

    class HomeView extends StatelessWidget {
        ... 
    }

<br>

## Deciding Class names

### Screens

When you're creating a class for some "screen" in the app then you will always use `View` as a suffix.<br>

Say, you want to create a class for "Home Screen".<br>
Your classname should be :

    class HomeView extends StatelessWidget {
        ...
    }


### Components

When you're creating a class for some component in the app then you will always use `Widget` as a suffix.<br>

Say, you want to create a class for "Bottom Navigation Button Component".<br>
Your classname should be :

    class BottomNavigationButtonWidget extends StatelessWidget {
        ...
    }


### Fragments

When you're creating a class for separating a small part of a screen with many components and some logic in the app then you will always use `Fragment` as a suffix.<br>

Say, you have a home screen which contains a listing widget then you can separate it from homeview into it's own component called as "Home View Listing Fragment".<br>
Your classname should be :

    class HomeViewListingFragment extends StatelessWidget {
        ...
    }

### Models

For Data Classes you'll use `Model` as a suffix.<br>

Suppose that creating a data class for an API response. Let the response be for "User profile".<br>
Your classname should be :

    class UserProfile {
        ...
    }

<br>

## Deciding Mixin names

When you create a mixin you'll use `Mixin` as a suffix.<br>
Say, you want to create a mixin for "Home".<br>
You're mixinname should be :

    mixin HomeMixin {
        ...
    }
    

