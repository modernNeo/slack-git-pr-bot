class ParseBitBucketWebHook:

    @staticmethod
    def parse_comment(payload):
        comment_info = payload['comment']
        comment = comment_info['content']
        # Gweujpr3edH1cvEE
