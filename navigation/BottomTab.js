import React from "react";
import HomeScreen from "../screens/HomeScreen";
import Recommended from "../screens/Recommended";
import Popular from "../screens/Popular";
import { Icon } from "react-native-elements";

import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
const Tab = createBottomTabNavigator();

const BottomTab = () => {
  //   const [url, setUrl] = React.useState("https://db3b-49-37-187-231.ngrok.io");
  //   const [movieDetails, setMovieDetails] = React.useState([]);

  //   React.useEffect(() => {
  //     getMovie();
  //   }, []);

  //   const timeConvert = (num) => {
  //     var hours = Math.floor(num / 60);
  //     var minutes = num % 60;
  //     return `${hours} hrs ${minutes} mins`;
  //   };

  //   const getMovie = () => {
  //     axios
  //       .get(url)
  //       .then((response) => {
  //         let details = response.data.data;
  //         details["duration"] = timeConvert(details.duration);
  //         setMovieDetails(details);
  //       })
  //       .catch((error) => {
  //         console.log(error.message);
  //       });
  //   };

  return (
    <Tab.Navigator
      initialRouteName="Home"
      screenOptions={{
        tabBarActiveTintColor: "#e91e63",
      }}
    >
      <Tab.Screen
        name="Home"
        component={HomeScreen}
        options={{
          tabBarLabel: "Home",
          tabBarIcon: ({ color, size }) => (
            <Icon name="home" type="feather" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Popular"
        component={Popular}
        options={{
          tabBarLabel: "Popular",
          tabBarIcon: ({ color, size }) => (
            <Icon name="trending-up" type="feather" color={color} size={size} />
          ),
          //   tabBarBadge: `${movieDetails.length}`,
        }}
      />
      <Tab.Screen
        name="Recommended"
        component={Recommended}
        options={{
          tabBarLabel: "Recommended",
          tabBarIcon: ({ color, size }) => (
            <Icon name="list" type="feather" color={color} size={size} />
          ),
        }}
      />
    </Tab.Navigator>
  );
};

export default BottomTab;
