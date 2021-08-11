import React, { useState, useEffect, useRef } from "react";
import {
    View,
    Text,
    StyleSheet,
    FlatList,
    TouchableOpacity,
} from "react-native";
import { Card } from "react-native-elements";
import ArticleModal from "./ArticleModal";

const CardComponent = (props) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [prevText, setPrevText] = useState("");
    const [prevCategory, setPrevCategory] = useState("All");
    const [firstParam, setFirstParam] = useState(10);
    const [secondParam, setSecondParam] = useState(19);
    const [fromFirst, setFromFirst] = useState(1);

    const flatListRef = useRef();

    const toTop = () => {
        flatListRef.current.scrollToOffset({ animated: true, index: -1 });
    };

    if (fromFirst !== props.fromFirst) {
        setFromFirst(props.fromFirst);
    }

    if (prevText !== props.search) {
        setPrevText(props.search);
    }

    if (prevCategory !== props.category) {
        setPrevCategory(props.category);
    }

    const extraLoadData = () => {
        fetch(props.pressURL, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                first: firstParam,
                last: secondParam,
                text: prevText,
                category: prevCategory,
            }),
        })
            .then((response) => response.json())
            .then((loadedData) => {
                let newData = data.concat(loadedData);
                setData(newData);
                setFirstParam(secondParam + 1);
                setSecondParam(secondParam + 10);
                setLoading(false);
            })
            .catch((e) => console.log(e));
    };

    const loadData = () => {
        fetch(props.pressURL, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                first: 0,
                last: 9,
                text: props.search,
                category: props.category,
            }),
        })
            .then((response) => response.json())
            .then((loadedData) => {
                setData(loadedData);
                setFirstParam(10);
                setSecondParam(19);
                setLoading(false);
            })
            .catch((e) => console.log(e));
    };

    const setTrue = (ID) => {
        setData(
            data.map((item) => {
                if (item.id === ID) {
                    return {
                        id: item.id,
                        title: item.title,
                        mainText: item.mainText,
                        visible: true,
                    };
                } else {
                    return item;
                }
            })
        );
    };

    const setFalse = (ID) => {
        setData(
            data.map((item) => {
                if (item.id === ID) {
                    return {
                        id: item.id,
                        title: item.title,
                        mainText: item.mainText,
                        visible: false,
                    };
                } else {
                    return item;
                }
            })
        );
    };

    useEffect(() => loadData(), []);

    useEffect(() => {
        setLoading(true);
        loadData();
        toTop();
    }, [prevText]);

    useEffect(() => {
        setLoading(true);
        loadData();
        toTop();
    }, [prevCategory]);

    useEffect(() => {
        toTop();
    }, [fromFirst]);

    const Item = ({ item }) => {
        return (
            <View>
                <ArticleModal item={item} FsetFalse={setFalse} />
                <TouchableOpacity onPress={() => setTrue(item.id)}>
                    <Card>
                        <Text style={styles.titleStyle2}>{item.title}</Text>
                        <Text></Text>
                        <Text numberOfLines={3}>{item.mainText}</Text>
                    </Card>
                </TouchableOpacity>
            </View>
        );
    };

    return (
        <View style={styles.container}>
            <FlatList
                style={{ width: "100%" }}
                data={data}
                renderItem={(item) => {
                    return Item(item);
                }}
                onRefresh={() => {
                    loadData();
                    setFirstParam(10);
                    setSecondParam(20);
                }}
                refreshing={loading}
                keyExtractor={(item) => item.id}
                onEndReached={() => {
                    setLoading(true);
                    extraLoadData();
                }}
                onEndReachedThreshold={0.9}
                ref={flatListRef}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignContent: "center",
        alignItems: "center",
        width: "100%",
    },
    titleStyle2: {
        fontSize: 20,
    },
});

export default CardComponent;
