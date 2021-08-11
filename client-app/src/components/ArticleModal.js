import React from "react";
import { View, Text, StyleSheet, Modal, ScrollView } from "react-native";
import { AntDesign } from "@expo/vector-icons";

const ArticleModal = (props) => {
    return (
        <Modal
            animationType="slide"
            transparent={false}
            visible={props.item.visible}
            onRequestClose={() => props.FsetFalse(props.item.id)}
        >
            <AntDesign.Button
                name="back"
                size={24}
                color="black"
                backgroundColor="white"
                onPress={() => {
                    props.FsetFalse(props.item.id);
                }}
                style={{ paddingLeft: 20 }}
            >
                <Text>뒤로 가기</Text>
            </AntDesign.Button>
            <ScrollView>
                <View style={styles.titleStyle}>
                    <Text style={styles.titleSize}>{props.item.title}</Text>
                </View>
                <View style={styles.articleStyle}>
                    <Text style={styles.titleSize}>{props.item.mainText}</Text>
                </View>
            </ScrollView>
        </Modal>
    );
};

const styles = StyleSheet.create({
    titleStyle: {
        margin: 20,
        backgroundColor: "white",
        borderRadius: 20,
        padding: 35,
        alignItems: "center",
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    articleStyle: {
        margin: 20,
        backgroundColor: "white",
        borderRadius: 20,
        padding: 35,
        alignItems: "center",
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    titleSize: {
        fontSize: 20,
    },
    articleSize: {
        fontSize: 15,
    },
});

export default ArticleModal;
