import React from 'react';
import { View, StyleSheet, Text, Platform, CheckBox } from 'react-native';
import { AntDesign } from '@expo/vector-icons';

const ScreenHeader = (props) => {
  return (
    <View style={styles.header}>
      <AntDesign.Button
        name="menuunfold"
        size={24}
        color="black"
        backgroundColor="white"
        onPress={() => props.navigation.toggleDrawer()}
      />
      <Text style={styles.text}>
        {props.screenName} : {props.categoryLabelValue}
      </Text>
      <View style={{ flexDirection: 'row' }}>
        <AntDesign.Button
          name="retweet"
          size={24}
          color="black"
          backgroundColor="white"
          style={{ marginleft: 3, marginRight: 0 }}
          onPress={() => {
            if (props.reset === 0) {
              props.FsetReset(1);
            } else {
              props.FsetReset(0);
            }
            props.FsetVisible1(false);
            props.FsetVisible2(false);
          }}
        />
        <AntDesign.Button
          name="search1"
          size={24}
          color="black"
          backgroundColor="white"
          style={{ marginleft: 0, marginRight: 0 }}
          onPress={() => {
            props.FsetVisible2(true);
          }}
        />
        <AntDesign.Button
          name="appstore1"
          size={24}
          color="black"
          backgroundColor="white"
          style={{ marginleft: 0, marginRight: 3 }}
          onPress={() => props.FsetVisible1(true)}
        />
      </View>
    </View>
  );
};
let styles;
if (Platform.OS === 'android') {
  styles = StyleSheet.create({
    header: {
      width: '100%',
      height: '8.5%',
      backgroundColor: 'white',
      alignItems: 'center',
      justifyContent: 'space-between',
      flexDirection: 'row',
      elevation: 3,
    },
    text: {
      marginLeft: '5%',
      textAlign: 'center',
      textAlignVertical: 'center',
      fontSize: 20,
    },
  });
} else {
  styles = StyleSheet.create({
    header: {
      width: '100%',
      height: '8.5%',
      backgroundColor: 'white',
      alignItems: 'center',
      justifyContent: 'space-between',
      flexDirection: 'row',
      shadowColor: '#000000',
      shadowOpacity: 0.3,
      shadowOffset: { width: 2, height: 2 },
    },
    text: {
      marginLeft: '5%',
      textAlign: 'center',
      textAlignVertical: 'center',
      fontSize: 20,
    },
  });
}

export default ScreenHeader;
