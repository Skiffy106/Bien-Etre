import {StyleSheet, Text, View} from 'react-native';
import React from 'react'
import {useLocalSearchParams} from "expo-router";

const UserDetails = () => {
    const { id } = useLocalSearchParams();
    return (
        <View>
            <Text>User Details: {id}</Text>
        </View>
    )
}
export default UserDetails;
const styles = StyleSheet.create({})