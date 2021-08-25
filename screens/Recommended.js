import React, { Component } from "react";
import { Text, View, TouchableOpacity, FlatList } from "react-native";
import { Card } from "react-native-elements";
import RFValue from "react-native-responsive-fontsize";
import axios from "axios";

export class Recommended extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      url: "https://db3b-49-37-187-231.ngrok.io",
      //   /popular-movies
    };
  }

  componentDidMount() {
    this.getData();
  }

  timeConvert(num) {
    var hours = Math.floor(num / 60);
    var minutes = num % 60;
    return `${hours} hrs ${minutes} mins`;
  }

  getData = () => {
    axios
      .get("https://db3b-49-37-187-231.ngrok.io/recommended-movies")
      .then(async (result) => {
        this.setState({ data: result.data.data });
      })
      .catch((error) => {
        console.log(error);
      });
  };

  render() {
    return (
      <View>
        <Text> Recommended </Text>
      </View>
    );
  }
}

export default Recommended;
