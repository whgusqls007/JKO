import React from "react";
import { View, StyleSheet, Text, TextInput } from "react-native";
import { AntDesign } from "@expo/vector-icons";

const SearchModalDetail = (props) => {
    return (
        <View style={{ backgroundColor: "white" }}>
            <Text
                style={{
                    paddingLeft: 30,
                    paddingTop: 30,
                    fontSize: 20,
                }}
            >
                검색
            </Text>
            <View
                style={{
                    marginLeft: 30,
                    marginTop: 20,
                    marginRight: 30,
                    marginBottom: 20,
                    borderWidth: 1,
                    height: 40,
                }}
            >
                <TextInput
                    style={{
                        marginLeft: 10,
                        marginRight: 10,
                        height: 40,
                    }}
                    placeholder="검색어"
                    value={props.tempTextValue}
                    onChangeText={props.FsetTempText}
                ></TextInput>
            </View>
            <View
                style={{
                    marginRight: 0,
                    marginLeft: "auto",
                    marginBottom: 20,
                    flexDirection: "row",
                }}
            >
                <AntDesign.Button
                    name="retweet"
                    size={24}
                    color="black"
                    style={{ backgroundColor: "white" }}
                    onPress={() => {
                        props.FsetText("");
                        props.FsetTempText("");
                        props.FsetVisible(false);
                    }}
                >
                    <Text>검색 초기화</Text>
                </AntDesign.Button>
                <AntDesign.Button
                    name="search1"
                    size={24}
                    color="black"
                    style={{ backgroundColor: "white" }}
                    onPress={() => {
                        props.FsetText(props.tempTextValue);
                        props.FsetVisible(false);
                    }}
                >
                    <Text>검색</Text>
                </AntDesign.Button>
                <AntDesign.Button
                    name="closecircle"
                    size={24}
                    color="black"
                    style={{ backgroundColor: "white" }}
                    onPress={() => props.FsetVisible(false)}
                >
                    <Text>닫기</Text>
                </AntDesign.Button>
            </View>
        </View>
    );
};

const styles = StyleSheet.create({});

export default SearchModalDetail;
